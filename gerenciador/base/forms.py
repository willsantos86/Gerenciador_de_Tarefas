from django import forms
from base.models import Tarefa

class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = [
            'responsavel', 'tarefa', 'data', 'status'
        ]