from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            'article_title',
            'article_content',
            'tags',
        ]
