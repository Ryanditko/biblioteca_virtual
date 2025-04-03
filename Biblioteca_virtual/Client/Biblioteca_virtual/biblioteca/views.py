from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Livro, Emprestimo, Categoria
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Conta criada com sucesso para {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})

def home(request):
    livros_recentes = Livro.objects.all().order_by('-id')[:8]
    categorias = Categoria.objects.all()
    context = {
        'livros_recentes': livros_recentes,
        'categorias': categorias,
    }
    return render(request, 'biblioteca/home.html', context)

def livro_list(request):
    livros = Livro.objects.all()
    query = request.GET.get('q')
    categoria = request.GET.get('categoria')

    if query:
        livros = livros.filter(
            Q(titulo__icontains=query) |
            Q(autor__icontains=query) |
            Q(isbn__icontains=query)
        )

    if categoria:
        livros = livros.filter(categoria__slug=categoria)

    paginator = Paginator(livros, 12)
    page = request.GET.get('page')
    livros = paginator.get_page(page)

    context = {
        'livros': livros,
        'categorias': Categoria.objects.all(),
    }
    return render(request, 'biblioteca/livro_list.html', context)

def livro_detail(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    context = {
        'livro': livro,
    }
    return render(request, 'biblioteca/livro_detail.html', context)

@login_required
def emprestimo_create(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    
    if not livro.disponivel:
        messages.error(request, 'Este livro não está disponível para empréstimo.')
        return redirect('biblioteca:livro_detail', pk=pk)

    emprestimo = Emprestimo.objects.create(
        livro=livro,
        usuario=request.user,
        data_emprestimo=timezone.now(),
        data_devolucao=timezone.now() + timezone.timedelta(days=14)
    )

    livro.disponivel = False
    livro.save()

    messages.success(request, 'Livro emprestado com sucesso!')
    return redirect('biblioteca:emprestimo_list')

@login_required
def emprestimo_list(request):
    emprestimos = Emprestimo.objects.filter(usuario=request.user).order_by('-data_emprestimo')
    context = {
        'emprestimos': emprestimos,
    }
    return render(request, 'biblioteca/emprestimo_list.html', context)

@login_required
def emprestimo_devolver(request, pk):
    emprestimo = get_object_or_404(Emprestimo, pk=pk, usuario=request.user)
    
    if emprestimo.devolvido:
        messages.error(request, 'Este livro já foi devolvido.')
        return redirect('biblioteca:emprestimo_list')

    emprestimo.devolvido = True
    emprestimo.data_devolucao_real = timezone.now()
    emprestimo.save()

    emprestimo.livro.disponivel = True
    emprestimo.livro.save()

    messages.success(request, 'Livro devolvido com sucesso!')
    return redirect('biblioteca:emprestimo_list')

def categoria_list(request):
    categorias = Categoria.objects.all()
    context = {
        'categorias': categorias,
    }
    return render(request, 'biblioteca/categoria_list.html', context)

def categoria_detail(request, slug):
    categoria = get_object_or_404(Categoria, slug=slug)
    livros = categoria.livros.all()

    paginator = Paginator(livros, 12)
    page = request.GET.get('page')
    livros = paginator.get_page(page)

    context = {
        'categoria': categoria,
        'livros': livros,
    }
    return render(request, 'biblioteca/categoria_detail.html', context)
