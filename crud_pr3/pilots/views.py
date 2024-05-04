from django.shortcuts import render, redirect
from .forms import PilotForm
from .models import Category, Pilots
# Create your views here.


def get_info(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'index.html', context=context)

def get_pilots(request, pk):
    pilots = pilots.objects.filter(category=pk)
    context = {
        'Pilots': pilots
    }
    return render(request, 'pilots.html', context=context)

def detail(request, pk):
    pilot = Pilots.objects.get(pk=pk)
    context = {
        'pilot': pilot
    }
    return render(request, 'detail.html', context=context)

def add_pilots(request):
    form = PilotForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('pilots:get_info')
    context = {
        'form': form
        }
    return render(request, 'create.html', context=context)


def update_pilots(request, pk):
    data = Pilots.objects.get(pk=pk)
    form = PilotForm(request.POST, request.FILES, instance=data)
    if form.is_valid():
        print(1)
        form.save()
        return redirect('pilots:get_info')
    context = {
        'form': form
        }
    return render(request, 'update.html', context=context)