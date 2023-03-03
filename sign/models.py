from django.db import models

class Info(models.Model):
    user_id = models.CharField(max_length=20, unique=True)
    user_pw = models.CharField(max_length=50)
