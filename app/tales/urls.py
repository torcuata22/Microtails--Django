from django.urls import path
from .views import(
    
    tale_create_view,
    tale_lookup_view, 
    tale_lookup_view, 
    tale_delete_view,
    tale_list_view,
)

app_name = 'tales'
urlpatterns = [
    path('tales/write', tale_create_view, name='create tale'),
    path('tales/details', tale_lookup_view, name='lookup tale'), #doesn't work
    path('<int:tale_id>/', tale_lookup_view, name='tale'),
    path('<int:tale_id>/tale_delete', tale_delete_view, name="delete-tale"), #list not showing up
    path('tale_list', tale_list_view, name="list-of-tales"),
]