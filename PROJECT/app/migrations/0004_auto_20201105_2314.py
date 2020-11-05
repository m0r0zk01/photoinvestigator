# Generated by Django 3.1.1 on 2020-11-05 20:14

import app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20201105_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='url',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='cardfile',
            name='file',
            field=models.FileField(upload_to=app.models.get_upload_path),
        ),
    ]
