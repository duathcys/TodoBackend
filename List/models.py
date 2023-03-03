from django.db import models
from django.db.models import CASCADE

from sign.models import Info


class Todo(models.Model):
    title = models.TextField()
    done = models.BooleanField(default=False)
    memo = models.TextField(default=None)
    info = models.ForeignKey(Info, to_field='user_id', max_length=50, on_delete=CASCADE)
