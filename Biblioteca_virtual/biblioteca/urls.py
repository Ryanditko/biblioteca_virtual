from django.urls import path
from . import views

app_name = 'biblioteca'

urlpatterns = [
    path('', views.home, name='home'),
    path('livros/', views.livro_list, name='livro_list'),
    path('livros/<int:pk>/', views.livro_detail, name='livro_detail'),
    path('livros/<int:pk>/emprestar/', views.emprestimo_create, name='emprestimo_create'),
    path('emprestimos/', views.emprestimo_list, name='emprestimo_list'),
    path('categorias/', views.categoria_list, name='categoria_list'),
    path('categorias/<slug:slug>/', views.categoria_detail, name='categoria_detail'),
] 