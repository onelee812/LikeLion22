from django.db import models

# Create your models here.

class Post(models.Model):

    title = models.CharField(max_length=30)
    content = models.TextField()
    view = models.IntegerField(default=0)

    def __str__(self):
        return self.title