from datetime import datetime

class Usuario:
    def __init__(self, nome: str, email: str, cpf: str):
        self.nome = nome
        self.email = email
        self.cpf = cpf
        self.data_cadastro = datetime.now()
        self.emprestimos = []
        self.ativo = True

    def pode_emprestar(self) -> bool:
        """Verifica se o usuário pode fazer empréstimos."""
        return self.ativo and len(self.emprestimos) < 3

    def desativar(self) -> None:
        """Desativa a conta do usuário."""
        self.ativo = False

    def ativar(self) -> None:
        """Ativa a conta do usuário."""
        self.ativo = True

    def __str__(self) -> str:
        return f"Usuário: {self.nome} - Email: {self.email}"

    def to_dict(self) -> dict:
        """Retorna o usuário em formato de dicionário."""
        return {
            "nome": self.nome,
            "email": self.email,
            "cpf": self.cpf,
            "data_cadastro": self.data_cadastro.isoformat(),
            "ativo": self.ativo
        } 