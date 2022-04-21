from django.shortcuts import render
from .models import Tales
from .forms import TalesForm, RawTaleForm

# Create your views here.

def tale_create_view(request):
    my_form = RawTaleForm()
    if request.method == "POST":
        my_form = RawTaleForm(request.POST)
        if my_form.is_valid():
            #now the data is good
            print(my_form.cleaned_data)
            Tales.objects.create(title= my_form.cleaned_data)
        else:
            print(my_form.errors)
    context={
            "form":my_form
         }
    return render (request, 'write.html', context)

# def tale_create_view(request):
#     form = TalesForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = TalesForm()

#     context={
#         'form': form
#     }

#     return render (request, 'write.html', context)


def tale_detail_view(request):
    obj=Tales.objects.get(id=15)
    #Long way around, but works:
    context={
        'title': obj.title,
        'author': obj.author,
        'genre': obj.genre,
        'content': obj.content
    }

    # Short way around, but doesn't work
    # context= {
    #     'object':obj
    # }
    return render(request, 'tales/details.html', context )
