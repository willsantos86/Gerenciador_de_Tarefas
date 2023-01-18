from django.shortcuts import render
from base.forms import *
from base.models import *
# Create your views here.

def tarefa(request):
    sucesso = False
    form = TarefaForm(request.POST or None)
    if form.is_valid():
        sucesso = True
        form.save()
    contexto = {
        'form': form,
        'sucesso': sucesso,
        'dados': Tarefa.objects.all(),
    }

    return render(request, 'tarefa.html', contexto)