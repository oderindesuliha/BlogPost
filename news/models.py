from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=1000)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def save(self, *args, **kwargs):
        if not self.title:
            self.title = self.content[:100]
            super(BlogPost, self).save(*args, **kwargs)

    def __str__(self):
        return self.title