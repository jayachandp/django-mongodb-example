from django.db import models

from djangotoolbox.fields import ListField

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=300)
    text = models.TextField()
    tags = ListField()
    comments = ListField()

    def __unicode__(self):
        return self.title
