# Generated by Django 4.1.3 on 2022-11-10 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medium', '0002_delete_note'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='author',
        ),
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.SlugField(default=None),
        ),
    ]
