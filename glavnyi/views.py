from django.shortcuts import render, redirect
from .models import Task, Madi, Parents
from .forms import TaskForm

# Create your views here.



def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'glavnyi/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})




def about(request):
    return render(request, 'glavnyi/about.html')


def madi(request):
    madi = Madi.object.order_by('id')
    return render(request, 'glavnyi/madi.html', {'madi': madi})




def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
                error = 'Форма была неверной'

    form = TaskForm()
    context = {
        'form': form,
        'error': error 
    }
    return render(request, 'glavnyi/create.html', context)
