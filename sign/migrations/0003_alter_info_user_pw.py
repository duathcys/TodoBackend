# Generated by Django 4.1.5 on 2023-08-18 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sign', '0002_info_createat_info_updateat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='user_pw',
            field=models.TextField(),
        ),
    ]