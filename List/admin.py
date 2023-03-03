from django.contrib import admin
from .models import Todo

@admin.register(Todo)
class InfoAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'done'
    )
# Register your models here.
