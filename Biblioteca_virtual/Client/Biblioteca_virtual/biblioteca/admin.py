from django.contrib import admin
from .models import Livro, Categoria, Emprestimo

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'icone', 'cor')
    search_fields = ('nome', 'descricao')
    list_filter = ('created_at',)

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'isbn', 'disponivel', 'categoria')
    search_fields = ('titulo', 'autor', 'isbn')
    list_filter = ('disponivel', 'categoria', 'ano_publicacao')
    date_hierarchy = 'created_at'

@admin.register(Emprestimo)
class EmprestimoAdmin(admin.ModelAdmin):
    list_display = ('livro', 'usuario', 'data_emprestimo', 'data_devolucao', 'status')
    search_fields = ('livro__titulo', 'usuario__username')
    list_filter = ('status', 'data_emprestimo', 'data_devolucao')
    date_hierarchy = 'data_emprestimo'
