from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)#input꼭최대길이적어줘야함
    content = models.TextField()#textarea

    def __str__(self):#객체를 문자열로 변환 
        return self.title
# Create your models here.
