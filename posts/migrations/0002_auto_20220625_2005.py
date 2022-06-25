# Generated by Django 3.2.9 on 2022-06-25 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='file',
        ),
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default='title', max_length=255),
            preserve_default=False,
        ),
    ]
