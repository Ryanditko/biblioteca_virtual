from datetime import datetime

class Livro:
    def __init__(self, titulo: str, autor: str, isbn: str, ano_publicacao: int, quantidade: int):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.ano_publicacao = ano_publicacao
        self.quantidade = quantidade
        self.quantidade_disponivel = quantidade
        self.data_cadastro = datetime.now()
        self.emprestimos = []

    def emprestar(self) -> bool:
        """Tenta emprestar um livro. Retorna True se bem sucedido, False caso contrário."""
        if self.quantidade_disponivel > 0:
            self.quantidade_disponivel -= 1
            return True
        return False

    def devolver(self) -> bool:
        """Tenta devolver um livro. Retorna True se bem sucedido, False caso contrário."""
        if self.quantidade_disponivel < self.quantidade:
            self.quantidade_disponivel += 1
            return True
        return False

    def __str__(self) -> str:
        return f"Livro: {self.titulo} - Autor: {self.autor} - ISBN: {self.isbn}"

    def to_dict(self) -> dict:
        """Retorna o livro em formato de dicionário."""
        return {
            "titulo": self.titulo,
            "autor": self.autor,
            "isbn": self.isbn,
            "ano_publicacao": self.ano_publicacao,
            "quantidade": self.quantidade,
            "quantidade_disponivel": self.quantidade_disponivel,
            "data_cadastro": self.data_cadastro.isoformat()
        } 