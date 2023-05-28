from django.db import models


# Create your models here.
class Annotation(models.Model):
    """ Annotation to be used for a text snippet """
    annotation = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """ Return string representation of the annotation """
        return self.label