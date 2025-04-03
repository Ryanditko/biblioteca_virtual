from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='biblioteca/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    # URLs de Livros
    path('livros/', views.livro_list, name='livro_list'),
    path('livros/<int:pk>/', views.livro_detail, name='livro_detail'),
    path('livros/criar/', views.livro_create, name='livro_create'),
    
    # URLs de Empréstimos
    path('emprestimos/', views.emprestimo_list, name='emprestimo_list'),
    path('emprestimos/criar/', views.emprestimo_create, name='emprestimo_create'),
    path('emprestimos/<int:pk>/devolver/', views.emprestimo_devolver, name='emprestimo_devolver'),
] 