from django.db import models

# Create your models here.
#전공모델 
class Major(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)

class Subject(models.Model):
    subject_name = models.CharField(max_length=255)
    major=models.ForeignKey('Major', on_delete=models.CASCADE, related_name="subject")
    prof_name=models.CharField(max_length=255)
    memo=models.TextField()

    def __str__(self):
        return str(self.subject_name)
