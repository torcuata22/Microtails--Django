from django.urls import path
from .views import (
    ArticleCreateView,
    ArticleDetailView,
    ArticleListView
    
)

app_name = 'articles'

urlpatterns = [
    path('', ArticleListView.as_view(), name= 'article_list'),
    path('create/', ArticleCreateView.as_view(), name= 'article_create'),
    path('<int:pk>', ArticleDetailView.as_view(), name= 'article_detail'),
    #path('<int:id>/update', view_name, name= 'article_update'),
    #path('<int:id>/delete', view_name, name= 'article_delete'),

]
