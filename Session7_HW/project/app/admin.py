from django.contrib import admin
from .models import Post #점을 붙이면 절대경로 아니면 상대경로
# Register your models here.

admin.site.register(Post)