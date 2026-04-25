from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('finalizar/<int:produto_id>/', views.finalizar_compra, name='finalizar_compra'),
    path('carrinho/', views.carrinho, name='carrinho'),
    path('remover/<int:pedido_id>/', views.remover_do_carrinho, name='remover_do_carrinho'),
]