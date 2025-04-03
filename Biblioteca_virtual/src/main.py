from models import Biblioteca, Livro, Usuario

def main():
    # Criando uma instância da biblioteca
    biblioteca = Biblioteca()

    # Cadastrando alguns livros
    livro1 = biblioteca.cadastrar_livro(
        titulo="O Senhor dos Anéis",
        autor="J.R.R. Tolkien",
        isbn="9788533613379",
        ano_publicacao=1954,
        quantidade=3
    )

    livro2 = biblioteca.cadastrar_livro(
        titulo="Harry Potter e a Pedra Filosofal",
        autor="J.K. Rowling",
        isbn="9788535909558",
        ano_publicacao=1997,
        quantidade=5
    )

    # Cadastrando alguns usuários
    usuario1 = biblioteca.cadastrar_usuario(
        nome="João Silva",
        email="joao@email.com",
        cpf="123.456.789-00"
    )

    usuario2 = biblioteca.cadastrar_usuario(
        nome="Maria Santos",
        email="maria@email.com",
        cpf="987.654.321-00"
    )

    # Realizando empréstimos
    emprestimo1 = biblioteca.emprestar_livro("9788533613379", "123.456.789-00")
    if emprestimo1:
        print(f"Empréstimo realizado com sucesso: {emprestimo1}")
    else:
        print("Não foi possível realizar o empréstimo")

    emprestimo2 = biblioteca.emprestar_livro("9788535909558", "987.654.321-00")
    if emprestimo2:
        print(f"Empréstimo realizado com sucesso: {emprestimo2}")
    else:
        print("Não foi possível realizar o empréstimo")

    # Listando livros disponíveis
    print("\nLivros disponíveis:")
    for livro in biblioteca.listar_livros_disponiveis():
        print(f"- {livro}")

    # Realizando uma devolução
    if biblioteca.devolver_livro("9788533613379", "123.456.789-00"):
        print("\nLivro devolvido com sucesso!")
    else:
        print("\nNão foi possível devolver o livro")

    # Listando empréstimos atrasados
    print("\nEmpréstimos atrasados:")
    for emprestimo in biblioteca.listar_emprestimos_atrasados():
        print(f"- {emprestimo}")

if __name__ == "__main__":
    main() 