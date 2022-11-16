from django.contrib import admin
from .models import Article, Author




class ArticleAdmin(admin.ModelAdmin):
    listDisplay = ("article_title", "article_content",)
    prepopulated_fields = {"slug": ("article_title",)}


admin.site.register(Article, ArticleAdmin)


class ArticleAuthor(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')


admin.site.register(Author)

