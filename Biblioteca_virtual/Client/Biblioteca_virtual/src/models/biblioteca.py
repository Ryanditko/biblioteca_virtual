from typing import List, Optional
from .livro import Livro
from .usuario import Usuario
from .emprestimo import Emprestimo

class Biblioteca:
    def __init__(self):
        self.livros: List[Livro] = []
        self.usuarios: List[Usuario] = []
        self.emprestimos: List[Emprestimo] = []

    def cadastrar_livro(self, titulo: str, autor: str, isbn: str, ano_publicacao: int, quantidade: int) -> Livro:
        """Cadastra um novo livro na biblioteca."""
        livro = Livro(titulo, autor, isbn, ano_publicacao, quantidade)
        self.livros.append(livro)
        return livro

    def cadastrar_usuario(self, nome: str, email: str, cpf: str) -> Usuario:
        """Cadastra um novo usuário na biblioteca."""
        usuario = Usuario(nome, email, cpf)
        self.usuarios.append(usuario)
        return usuario

    def emprestar_livro(self, isbn: str, cpf: str) -> Optional[Emprestimo]:
        """Realiza o empréstimo de um livro para um usuário."""
        livro = self.buscar_livro_por_isbn(isbn)
        usuario = self.buscar_usuario_por_cpf(cpf)

        if not livro or not usuario:
            return None

        if not usuario.pode_emprestar() or not livro.emprestar():
            return None

        emprestimo = Emprestimo(livro, usuario)
        self.emprestimos.append(emprestimo)
        usuario.emprestimos.append(emprestimo)
        livro.emprestimos.append(emprestimo)

        return emprestimo

    def devolver_livro(self, isbn: str, cpf: str) -> bool:
        """Realiza a devolução de um livro."""
        emprestimo = self.buscar_emprestimo_ativo(isbn, cpf)
        if emprestimo:
            return emprestimo.devolver()
        return False

    def buscar_livro_por_isbn(self, isbn: str) -> Optional[Livro]:
        """Busca um livro pelo ISBN."""
        for livro in self.livros:
            if livro.isbn == isbn:
                return livro
        return None

    def buscar_usuario_por_cpf(self, cpf: str) -> Optional[Usuario]:
        """Busca um usuário pelo CPF."""
        for usuario in self.usuarios:
            if usuario.cpf == cpf:
                return usuario
        return None

    def buscar_emprestimo_ativo(self, isbn: str, cpf: str) -> Optional[Emprestimo]:
        """Busca um empréstimo ativo por ISBN e CPF."""
        for emprestimo in self.emprestimos:
            if (emprestimo.livro.isbn == isbn and 
                emprestimo.usuario.cpf == cpf and 
                not emprestimo.devolvido):
                return emprestimo
        return None

    def listar_livros_disponiveis(self) -> List[Livro]:
        """Lista todos os livros disponíveis para empréstimo."""
        return [livro for livro in self.livros if livro.quantidade_disponivel > 0]

    def listar_emprestimos_atrasados(self) -> List[Emprestimo]:
        """Lista todos os empréstimos atrasados."""
        return [emprestimo for emprestimo in self.emprestimos 
                if emprestimo.esta_atrasado() and not emprestimo.devolvido] 