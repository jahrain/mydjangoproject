from django.db import models
from django.contrib import admin


class Post(models.Model):
    title = models.CharField(max_length=120)
    posted_at = models.DateField()
    body = models.TextField()
    posted_by = models.CharField(max_length=40, null=True)
    
    def __unicode__(self):
        return self.title
    
admin.site.register(Post) 