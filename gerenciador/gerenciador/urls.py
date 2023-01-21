
from django.contrib import admin
from django.urls import path, include
from base.views import *

app_name= 'base'

urlpatterns = [
    
    path('deletar/<int:pk>/', deletar, name='deletar'),
    path('tarefa/', tarefa, name='tarefa'),
    path('editar/<int:pk>/', editar, name="editar"),
    path('visualizar/', visualizar, name='visualizar'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
]
