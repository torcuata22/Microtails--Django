from django.shortcuts import render
from .models import Tales

# Create your views here.
def tale_detail_view(request):
    obj=Tales.objects.get(id=15)
    #Long way around, but works:
    context={
        'title': obj.title,
        'author': obj.author,
        'genre': obj.genre,
        'date_created': obj.date_created,
        'content': obj.content
    }

    # Short way around, but doesn't work
    # context= {
    #     'object':obj
    # }
    return render(request, 'tales/details.html', context )
