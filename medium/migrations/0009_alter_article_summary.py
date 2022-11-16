# Generated by Django 4.1.3 on 2022-11-13 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medium', '0008_alter_article_author_delete_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='summary',
            field=models.TextField(help_text='Enter a brief description of the article', max_length=1000, null=True),
        ),
    ]
