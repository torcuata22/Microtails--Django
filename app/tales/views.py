from django.shortcuts import render, get_object_or_404, redirect
from .models import Tales
from .forms import TalesForm

# Create your views here.

def tale_lookup_view(request, tale_id):
    #obj = Tales.objects.get(id= tale_id)
    obj = get_object_or_404(Tales, id = tale_id)
    context = {
        'object': obj
    }

    return render (request, 'tales/details.html', context)

def tale_delete_view (request, tale_id):
    obj = get_object_or_404 (Tales, id = tale_id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../../')
    context = { "object": obj}

    return render (request, 'tales/tale_delete.html', context)



# def render_initial_data(request):
#     initial_data = {
#         'title':'Your Title',
#         'author': 'Your name',
#         'genre' : 'What genre is your story?',
#         'content': 'Write your story!' 

#     }
#     form = TalesForm(request.POST or None)
#     context = {
#         'form': form
#     }
#     return render (request, 'write.html', context)


def tale_create_view(request):
    my_form = TalesForm(request.POST or None)
    if my_form.is_valid():
        my_form.save()
        my_form = TalesForm()

    context={
        'form': my_form
    }

    return render (request, 'write.html', context)


def tale_detail_view(request, id):
    obj=Tales.objects.get(id)
    context={
        'title': obj.title,
        'author': obj.author,
        'genre': obj.genre,
        'content': obj.content
    }
    return render(request, 'tales/details.html', context )
    # Short way around, but doesn't work
    # context= {
    #     'object':obj
    # }

def tale_list_view(request):
    queryset = Tales.objects.all()
    context = {
        "object_list": queryset
    }
    return render (request, 'tales/tale_list.html', context)


# def tale_create_view(request):
#     my_form = RawTaleForm()
#     if request.method == "POST":
#         my_form = RawTaleForm(request.POST)
#         if my_form.is_valid():
#             #now the data is good
#             print(my_form.cleaned_data)
#             Tales.objects.create(title= my_form.cleaned_data)
#         else:
#             print(my_form.errors)
#     context={
#             "form":my_form
#          }
#     return render (request, 'write.html', context)