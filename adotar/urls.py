from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_pets, name="listar_pets"),
    path('processa_pedido_adocao/<int:id_pedido>', views.processa_pedido_adocao, name="processa_pedido_adocao"),        
    
]
