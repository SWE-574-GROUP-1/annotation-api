from rest_framework import viewsets
from .models import Annotation
from .serializers import AnnotationSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404, JsonResponse
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


class AnnotationViewSet(viewsets.ModelViewSet):
    queryset = Annotation.objects.all()
    serializer_class = AnnotationSerializer

    def create(self, request, *args, **kwargs):
        annotation_data = request.data
        annotation_id = annotation_data["id"]
        annotation_target = annotation_data["target"]
        annotation_body = annotation_data["body"]
        created_at = annotation_data["created"]
        created_by = annotation_data["creator"]
        url = annotation_data["target"]["source"]

        if annotation_target["selector"]["type"] == "FragmentSelector":
            annotation_type = "image"
            index = annotation_id.find("/annotations")

            if index != -1:
                # Remove the part starting from "/annotations"
                url = annotation_id[:index]

        else:
            annotation_type = "text"

        Annotation.objects.create(
            annotation_id=annotation_id,
            annotation_target=annotation_target,
            annotation_body=annotation_body,
            annotation_type=annotation_type,
            created_at=created_at,
            created_by=created_by,
            url=url
        )

        return JsonResponse({
            "annotation_id": annotation_id,
            "annotation_target": annotation_target,
            "annotation_body": annotation_body,
            "created_at": created_at,
            "created_by": created_by,
            "url": url
        }, status=201)


class AnnotationSearch(APIView):
    def get(self, request):
        query = request.GET.get("query", "")
        if not query:
            return JsonResponse({"error": "Missing query parameter"}, status=400)

        annotations = Annotation.objects.filter(Q(url__icontains=query))
        # order by annotation_type desc
        annotations = annotations.order_by('-annotation_type')
        annotations = [annotation.as_dict() for annotation in annotations]
        # order by 
        return JsonResponse(annotations, safe=False, status=200)