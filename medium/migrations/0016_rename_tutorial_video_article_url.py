# Generated by Django 4.1.3 on 2022-11-16 04:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medium', '0015_article_tutorial_video_alter_article_thumbnail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='tutorial_Video',
            new_name='url',
        ),
    ]