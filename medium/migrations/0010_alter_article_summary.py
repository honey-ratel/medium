# Generated by Django 4.1.3 on 2022-11-13 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medium', '0009_alter_article_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='summary',
            field=models.TextField(help_text='Enter a brief description of the article', max_length=1000),
        ),
    ]
