from django.views.generic import ListView, DetailView
from .models import Article
from django.core.paginator import Paginator, EmptyPage


class ArticleDetailView(DetailView):
    model = Article
    template_name = "articles/article_detail.html"

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        object = contex['object']
        first_half = object.article_content[:400]
        second_half = object.article_content[400:]
        contex['first_half'] = first_half
        contex['second_half'] = second_half
        return contex


class TagRecentView(ListView):
    model = Article

    def get_queryset(self):
        tag_list = Article.objects.filter(tags__name=self.kwargs['tag'])
        return tag_list

    template_name = "articles/tag_list.html"


class BootRecentView(ListView):
    model = Article
    template_name = "articles/boot_strap.html"
    paginate_by = 5
    ordering = ['-date']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page = self.request.GET.get('page', 1)
        articles = Article.objects.all().order_by('-date')

        paginator = self.paginator_class(articles, self.paginate_by)

        users = paginator.page(page)

        context['users'] = users
        return context


class MyPaginator(Paginator):
    def validate_number(self, number):
        try:
            return super().validate_number(number)
        except EmptyPage:
            if int(number) > 1:

                return self.num_pages
            elif int(number) < 1:

                return 1
            else:
                raise
