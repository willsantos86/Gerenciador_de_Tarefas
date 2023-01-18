from django.contrib import admin
from base.models import Tarefa, Pessoas

# Register your models here.
class TarefaAdmin(admin.ModelAdmin):
    pass

class PessoasAdmin(admin.ModelAdmin):
    pass

admin.site.register(Tarefa, TarefaAdmin)
admin.site.register(Pessoas, PessoasAdmin)