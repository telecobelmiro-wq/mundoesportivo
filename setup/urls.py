from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Redireciona a página inicial vazia direto para a sua tela de livros
    path('', lambda request: redirect('gerenciar_livros'), name='root_redirect'),
    
    path('', include('core.urls')),
]