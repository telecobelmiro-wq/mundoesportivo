from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'livros', views.LivroViewSet, basename='api-livros')
router.register(r'emprestimos', views.EmprestimoViewSet, basename='api-emprestimos')

urlpatterns = [
    path('gerenciamento/livros/', views.gerenciar_livros, name='gerenciar_livros'),
    path('gerenciamento/emprestimos/', views.gerenciar_emprestimos, name='gerenciar_emprestimos'),
    path('api/', include(router.urls)),
]