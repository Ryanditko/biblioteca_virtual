from django.core.management.base import BaseCommand
from biblioteca.models import Categoria

class Command(BaseCommand):
    help = 'Adiciona as categorias iniciais ao banco de dados'

    def handle(self, *args, **kwargs):
        categorias = [
            {
                'nome': 'Ficção',
                'descricao': 'Livros de ficção, incluindo romances, contos e ficção científica.',
                'icone': 'bi-book',
                'cor': '#6c5ce7'
            },
            {
                'nome': 'Não Ficção',
                'descricao': 'Livros baseados em fatos reais, biografias e documentários.',
                'icone': 'bi-journal-text',
                'cor': '#00b894'
            },
            {
                'nome': 'Literatura Infantil',
                'descricao': 'Livros para crianças e jovens leitores.',
                'icone': 'bi-rainbow',
                'cor': '#ff7675'
            },
            {
                'nome': 'História',
                'descricao': 'Livros sobre eventos históricos e períodos específicos.',
                'icone': 'bi-clock-history',
                'cor': '#fdcb6e'
            },
            {
                'nome': 'Ciência',
                'descricao': 'Livros sobre ciências, tecnologia e descobertas.',
                'icone': 'bi-flask',
                'cor': '#74b9ff'
            },
            {
                'nome': 'Arte e Cultura',
                'descricao': 'Livros sobre artes, música, cinema e cultura geral.',
                'icone': 'bi-palette',
                'cor': '#a8a4e6'
            },
            {
                'nome': 'Autoajuda',
                'descricao': 'Livros para desenvolvimento pessoal e bem-estar.',
                'icone': 'bi-heart',
                'cor': '#ff9ff3'
            },
            {
                'nome': 'Poesia',
                'descricao': 'Coleções de poesias e poemas.',
                'icone': 'bi-pencil',
                'cor': '#55efc4'
            }
        ]
        
        for categoria in categorias:
            Categoria.objects.get_or_create(**categoria)
            self.stdout.write(self.style.SUCCESS(f'Categoria "{categoria["nome"]}" criada com sucesso!')) 