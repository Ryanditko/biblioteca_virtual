from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Livro, Usuario, Emprestimo

class UserRegistrationForm(UserCreationForm):
    cpf = forms.CharField(max_length=14, required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'cpf', 'password1', 'password2')

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['titulo', 'autor', 'isbn', 'ano_publicacao', 'quantidade', 'descricao', 'categoria', 'imagem']
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 4}),
        }

class EmprestimoForm(forms.ModelForm):
    class Meta:
        model = Emprestimo
        fields = ['livro', 'usuario', 'data_prevista_devolucao']
        widgets = {
            'data_prevista_devolucao': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        } 