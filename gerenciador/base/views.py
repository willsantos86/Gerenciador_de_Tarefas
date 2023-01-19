from django.shortcuts import render,redirect
from base.forms import *
from base.models import *
# Create your views here.

def tarefa(request):
    listas = Tarefa.objects.all()
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    form = TarefaForm()
    contexto = {
        'form': form,
        'listas': listas 
    }
    return render(request, 'tarefa.html', contexto)


def visualizar(request):
    listas = Tarefa.objects.all()

    contexto = {
        'listas': listas,
    }
    return render(request, 'tarefa.html', contexto)