from django.urls import path
from .views import (
    ArticleCreateView,
    ArticleDetailView,
    ArticleDeleteView,
    ArticleListView,
    ArticleUpdateView
    
)

app_name = 'articles'

urlpatterns = [
    path('', ArticleListView.as_view(), name= 'article_list'),#working
    path('create/', ArticleCreateView.as_view(), name= 'article_create'), #working
    path('<int:id>', ArticleDetailView.as_view(), name= 'article_detail'), #working
    path('<int:id>/update', ArticleUpdateView.as_view(), name= 'article_update'), #it is not updating the article
    path('<int:id>/delete', ArticleDeleteView.as_view(), name= 'article_delete'),#link works, but doesn't delete article 

]
