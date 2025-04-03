from datetime import datetime, timedelta
from .livro import Livro
from .usuario import Usuario

class Emprestimo:
    def __init__(self, livro: Livro, usuario: Usuario):
        self.livro = livro
        self.usuario = usuario
        self.data_emprestimo = datetime.now()
        self.data_prevista_devolucao = self.data_emprestimo + timedelta(days=15)
        self.data_devolucao = None
        self.devolvido = False

    def devolver(self) -> bool:
        """Registra a devolução do livro."""
        if not self.devolvido:
            self.data_devolucao = datetime.now()
            self.devolvido = True
            self.livro.devolver()
            return True
        return False

    def esta_atrasado(self) -> bool:
        """Verifica se o empréstimo está atrasado."""
        if not self.devolvido:
            return datetime.now() > self.data_prevista_devolucao
        return False

    def __str__(self) -> str:
        status = "Devolvido" if self.devolvido else "Em andamento"
        return f"Empréstimo: {self.livro.titulo} - {self.usuario.nome} - Status: {status}"

    def to_dict(self) -> dict:
        """Retorna o empréstimo em formato de dicionário."""
        return {
            "livro": self.livro.to_dict(),
            "usuario": self.usuario.to_dict(),
            "data_emprestimo": self.data_emprestimo.isoformat(),
            "data_prevista_devolucao": self.data_prevista_devolucao.isoformat(),
            "data_devolucao": self.data_devolucao.isoformat() if self.data_devolucao else None,
            "devolvido": self.devolvido
        } 