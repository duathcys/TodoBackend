# Generated by Django 4.1.5 on 2023-08-16 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('List', '0002_alter_category_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='priority',
        ),
    ]
