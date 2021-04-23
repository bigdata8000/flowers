from django.shortcuts import render, get_object_or_404
from .models import Flower
from django.http import HttpResponseRedirect
from .forms import MyForm

def index(request):

    q = request.GET.get('q', None)
    flowers = ''

    if q == None or q == "":
        flowers = Flower.objects.all()
    elif q is not None:
        flowers = Flower.objects.filter(title__contains=q)

    return render(request, 'myapp/index.html', {'flowers': flowers})


def detail(request, id=None):
    flower = get_object_or_404(Flower, id=id)
    return render(request, 'myapp/detail.html', {'flower': flower})


def create(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = MyForm()
    return render(request, 'myapp/edit.html', {'form': form})


def edit(request, id=None):
    flower = get_object_or_404(Flower, id=id)
    if request.method == 'POST':
        form = MyForm(request.POST, instance=flower)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = MyForm(instance=flower)
    return render(request, 'myapp/edit.html', {'form': form})

