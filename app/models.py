from django.db import models


# Create your models here.
class Annotation(models.Model):
    """ Annotation to be used for a text snippet """
    annotation_id = models.CharField(max_length=255, blank=True)
    url = models.URLField(max_length=500, blank=True)
    annotation_type = models.CharField(max_length=10, blank=True)
    annotation_body = models.JSONField(blank=True)
    annotation_target = models.JSONField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    created_by = models.IntegerField(blank=True, null=True)

    def __str__(self):
        """ Return string representation of the annotation """
        return self.label

    def as_dict(self):
        """ Return annotation as dictionary """
        ldp = {
            "@context": "http://www.w3.org/ns/anno.jsonld",
            "id": self.annotation_id,
            "type": "Annotation",
            "motivation": "highlighting",
            "created": self.created_at,
            "target": self.annotation_target,
            "body": self.annotation_body,
            "creator": self.created_by
        }

        return ldp
