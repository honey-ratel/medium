from django.urls import path
from .views import ArticleDetailView, TagRecentView, BootRecentView

urlpatterns = [
    path("", BootRecentView.as_view(), name="boot_strap"),
    path("<slug:slug>/", ArticleDetailView.as_view(), name="article_detail"),
    path("tag/<slug:tag>/", TagRecentView.as_view(), name="tag_list"),
]
