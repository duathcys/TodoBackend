# Generated by Django 4.1.5 on 2023-02-20 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('done', models.BooleanField(default=False)),
                ('memo', models.TextField(default=None)),
            ],
        ),
    ]