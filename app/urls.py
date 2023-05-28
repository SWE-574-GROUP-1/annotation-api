from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AnnotationViewSet, AnnotationSearch

router = DefaultRouter()
router.register('annotations', AnnotationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path("annotations/search", AnnotationSearch.as_view(), name="annotation_search"),
]
