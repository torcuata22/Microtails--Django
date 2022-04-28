from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    ListView,
    DeleteView
)
from .forms import ArticleModelForm
from .models import Article

class ArticleCreateView(CreateView):
    template_name = 'articles/article_create.html'
    form_class = ArticleModelForm
    queryset = Article.objects.all()

class ArticleListView(ListView):
    template_name = 'articles/article_list.html'
    queryset = Article.objects.all() # blog/<modelname>_list.html 

class ArticleDetailView(DetailView):
    template_name = 'articles/article_detail.html'
    queryset = Article.objects.all() 

    # def get_object(self):
    #     id = self.kwargs.get('id')
    #     return get_object_or_404 (Article, id = id)
    # not working as intended, so went back to pk
