from django.db import models
from django.contrib.auth.models import User

class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13, unique=True)
    ano_publicacao = models.IntegerField()
    quantidade = models.IntegerField()
    quantidade_disponivel = models.IntegerField()
    data_cadastro = models.DateTimeField(auto_now_add=True)
    imagem = models.ImageField(upload_to='livros/', null=True, blank=True)
    descricao = models.TextField(blank=True)
    categoria = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.titulo} - {self.autor}"

    class Meta:
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=14, unique=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.cpf}"

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

class Emprestimo(models.Model):
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    data_emprestimo = models.DateTimeField(auto_now_add=True)
    data_prevista_devolucao = models.DateTimeField()
    data_devolucao = models.DateTimeField(null=True, blank=True)
    devolvido = models.BooleanField(default=False)

    def __str__(self):
        status = "Devolvido" if self.devolvido else "Em andamento"
        return f"{self.livro.titulo} - {self.usuario.user.get_full_name()} - {status}"

    class Meta:
        verbose_name = 'Empréstimo'
        verbose_name_plural = 'Empréstimos' 