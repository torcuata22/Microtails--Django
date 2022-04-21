from django.shortcuts import render
from .models import Tales
from .forms import TalesForm

# Create your views here.
def tale_create_view(request):
    form = TalesForm(request.POST or None)
    if form.is_valid():
        form.save

    context={
        'form': form
    }

    return render (request, 'tales/tale_create.html', context)

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
