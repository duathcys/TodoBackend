from django.db import models


class Info(models.Model):
    user_id = models.CharField(max_length=20, unique=True)
    user_pw = models.TextField()
    nickname = models.CharField(max_length=20, null=True, default=None)
    createAt = models.DateTimeField(auto_now_add=True)
    updateAt = models.DateTimeField(auto_now=True)
