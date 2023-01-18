from django import forms
from base.models import Tarefa

class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = [
            'setor', 'responsavel', 'tarefa', 'data', 'status'
        ]