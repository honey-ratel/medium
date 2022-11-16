# Generated by Django 4.1.3 on 2022-11-08 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('articleTitle', models.CharField(max_length=100)),
                ('articleContent', models.TextField()),
                ('date', models.DateTimeField(auto_now=True)),
                ('thumbnail', models.ImageField(blank=True, default='default.png', upload_to='')),
                ('summary', models.TextField(help_text='Enter a brief description of the article', max_length=1000)),
                ('author', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='medium.author')),
            ],
        ),
    ]
