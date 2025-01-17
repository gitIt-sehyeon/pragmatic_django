from django.contrib.auth.models import User
from django.db import models

# Create your models here.

#auto_created=True -> auto_now_add=True 로 변경해야됨

class Article(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='article', null=True)

    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='article/', null=False)
    content = models.TextField(null=True)

    created_at = models.DateField(auto_created=True, null=True)
