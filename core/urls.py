from django.urls import path
from . import views

urlpatterns = [
    # Rota principal usando a função 'home'
    path('', views.home, name='home'),
    
    # Rota de detalhes usando a função 'produto_detail'
    path('produto/<int:pk>/', views.produto_detail, name='produto_detail'),

    # Rotas do carrinho e finalização (Funções)
    path('carrinho/', views.carrinho, name='carrinho'),
    path('finalizar/<int:produto_id>/', views.finalizar_compra, name='finalizar_compra'),
    path('remover/<int:pedido_id>/', views.remover_do_carrinho, name='remover_do_carrinho'),
    path('finalizar-carrinho/', views.finalizar_carrinho, name='finalizar_carrinho'),
]