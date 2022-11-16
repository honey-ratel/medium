from django.core.files.storage import FileSystemStorage
from django.template.defaultfilters import slugify  # new
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from djangoProject1 import settings
from embed_video.fields import EmbedVideoField


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    author_description = models.TextField(max_length=1000, help_text='Enter a brief description of your self',
                                          blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'


class Article(models.Model):
    article_title = models.CharField(max_length=100)
    slug = models.SlugField(null=False, unique=True)
    article_content = models.TextField()
    date = models.DateTimeField(auto_now=True)
    thumbnail = models.FileField(storage=FileSystemStorage(location=settings.MEDIA_ROOT), upload_to='uploads/%Y/%m/%d/',
                                 default='settings.MEDIA_ROOT/default_photo.jpg')

    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the article', blank=True)
    tags = TaggableManager(blank=True)
    url = EmbedVideoField(blank=True)
    image = models.ImageField(storage=FileSystemStorage(location=settings.MEDIA_ROOT), upload_to='uploads/%Y/%m/%d/',
                              default='settings.MEDIA_ROOT/default_photo.jpg')

    def __str__(self):
        return self.article_title

    def snippet(self):
        if self.summary != '':
            return self.summary
        return self.article_content[:110] + '...'

    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.article_title)
        return super().save(*args, **kwargs)

    def reading_time(self):
        if round(len(self.article_content) / 200) <= 0:
            return 1
        return round(len(self.article_content) / 200)
