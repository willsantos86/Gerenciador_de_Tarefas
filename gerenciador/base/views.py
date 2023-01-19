from django.shortcuts import render,redirect
from base.forms import *
from base.models import *
from django.core.paginator import Paginator
# Create your views here.

def tarefa(request):
    listas = Tarefa.objects.all()
    paginator = Paginator(listas, 2)
    page = request.GET.get('page')
    pagina = paginator.get_page(page)

    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    form = TarefaForm()
    contexto = {
        'form': form,
        'listas': listas,
        'pagina': pagina,
    }
    return render(request, 'tarefa.html', contexto)


def editar(request, pk):
    tarefa = Tarefa.objects.get(id=pk)
    form = TarefaForm(instance=tarefa)
    context = {'form': form}

    if request.method =='POST':
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'editar.html', context)
