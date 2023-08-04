from django.db import models
from django.db.models import CASCADE

from sign.models import Info


class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)
    priority = models.IntegerField()

    # class Meta:
    #     db_table = 'list_category'


class Todo(models.Model):
    title = models.TextField()
    done = models.BooleanField(default=False)
    memo = models.TextField(default=None)
    createAt = models.DateTimeField(auto_now_add=True)
    updateAt = models.DateTimeField(auto_now=True)
    dueDate = models.CharField(max_length=10, default=None)
    category = models.ForeignKey(Category, to_field='name', on_delete=CASCADE)
    info = models.ForeignKey(Info, to_field='user_id', max_length=50, on_delete=CASCADE)
