from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    icone = models.CharField(max_length=50, help_text='Classe do ícone do Bootstrap Icons')
    cor = models.CharField(max_length=7, help_text='Cor em formato hexadecimal (ex: #6c5ce7)')
    slug = models.SlugField(unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['nome']

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nome)
        super().save(*args, **kwargs)

class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13, unique=True)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='livros/', null=True, blank=True)
    ano_publicacao = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, related_name='livros')
    disponivel = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'
        ordering = ['-created_at']

    def __str__(self):
        return self.titulo

class Emprestimo(models.Model):
    STATUS_CHOICES = [
        ('emprestado', 'Emprestado'),
        ('devolvido', 'Devolvido'),
        ('atrasado', 'Atrasado'),
    ]

    livro = models.ForeignKey(Livro, on_delete=models.CASCADE, related_name='emprestimos')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='emprestimos')
    data_emprestimo = models.DateTimeField(auto_now_add=True)
    data_devolucao = models.DateTimeField()
    data_devolucao_real = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='emprestado')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Empréstimo'
        verbose_name_plural = 'Empréstimos'
        ordering = ['-data_emprestimo']

    def __str__(self):
        return f'{self.livro.titulo} - {self.usuario.username}'

    @property
    def atrasado(self):
        return self.status == 'atrasado' or (self.status == 'emprestado' and timezone.now() > self.data_devolucao)

    def save(self, *args, **kwargs):
        if self.data_devolucao_real:
            self.status = 'devolvido'
        elif self.atrasado:
            self.status = 'atrasado'
        if self.status == 'devolvido' and not self.data_devolucao_real:
            self.data_devolucao_real = timezone.now()
        super().save(*args, **kwargs)
