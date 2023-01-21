from django.shortcuts import render,redirect
from base.forms import *
from django.core.paginator import Paginator
# Create your views here.


def inicio(request):
    dados = []
    dados.append (
        {
            'destaque': 'Destaque',
            'titulo': 'Cabeça Fria Coração Quente',
            'autor': 'Abel Ferreira',
            'trecho': 'Uma viagem pelos bastidores da equipa tecnica: Segredos, reflexões e metodos de trabalho revelados em primeira pessoa.'
        }
    )
    dados.append (
        {
            'destaque': 'Destaque',
            'titulo': 'Python e Django',
            'autor': 'Francisco Marcelo',
            'trecho': 'Desenvolvimento web moderno e ágil.'
        }
    )
    contexto = {
        'dados': dados
    }
    return render(request,'inicio.html', contexto)


def tarefa(request):
    sucesso = False
    form = TarefaForm(request.POST or None)
    if form.is_valid():
        sucesso = True
        form.save()
    contexto = {
        'form': form,
        'sucesso': sucesso,
    }
    return render(request, 'tarefa.html', contexto)


def visualizar(request):
    tarefa = Tarefa.objects.all()
    paginator = Paginator(tarefa, 5)
    page = request.GET.get('page')
    tarefas = paginator.get_page(page)
    context = {'tarefas': tarefas,}
    return render(request,'visualizar.html', context)

def editar(request, pk):
    tarefa = Tarefa.objects.get(id=pk)
    form = TarefaForm(instance= tarefa )
    context = {'form': form}

    if request.method =='POST':
        form = TarefaForm(request.POST, instance= tarefa)

        if form.is_valid():
            form.save()
            return redirect('visualizar')
    return render(request, 'editar.html', context)


def deletar(request, pk):
    tarefa = Tarefa.objects.get(id=pk)
    tarefa.delete()
    return redirect('visualizar')

