# 📚 Biblioteca Virtual

Um projeto de biblioteca virtual desenvolvido com Django para aprender sobre desenvolvimento web. Este projeto foi criado como parte do meu processo de aprendizagem, utilizando IA (Claude) como par de programação.

## 🎯 Objetivo do Projeto

Este projeto foi desenvolvido com o propósito educacional de:
- Aprender os fundamentos do Django
- Entender o desenvolvimento de aplicações web
- Praticar a integração de front-end com back-end
- Explorar o desenvolvimento assistido por IA

## 🛠️ Tecnologias Utilizadas

- Python 3.12
- Django 5.0.2
- Bootstrap 5
- SQLite3
- HTML/CSS
- Bootstrap Icons

## 📋 Funcionalidades

- Sistema de autenticação (login/registro)
- Catálogo de livros
- Categorização de livros
- Sistema de empréstimos
- Painel administrativo
- Interface responsiva e moderna

## 🚀 Como Executar o Projeto

1. Clone o repositório
```bash
git clone https://github.com/ryanditko/biblioteca_virtual.git
cd biblioteca_virtual
```

2. Crie um ambiente virtual e ative-o
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Instale as dependências
```bash
pip install -r requirements.txt
```

4. Execute as migrações
```bash
python manage.py migrate
```

5. Crie um superusuário
```bash
python manage.py createsuperuser
```

6. Inicie o servidor
```bash
python manage.py runserver
```

7. Acesse http://127.0.0.1:8000/ no seu navegador

## 📁 Estrutura do Projeto

```
biblioteca_virtual/
├── biblioteca/              # Aplicação principal
│   ├── migrations/         # Migrações do banco de dados
│   ├── templates/         # Templates HTML
│   ├── static/           # Arquivos estáticos (CSS, JS, imagens)
│   ├── admin.py         # Configuração do painel administrativo
│   ├── models.py        # Modelos do banco de dados
│   ├── views.py         # Lógica das views
│   ├── urls.py          # URLs da aplicação
│   └── forms.py         # Formulários
├── biblioteca_virtual/   # Configurações do projeto
├── media/               # Arquivos de mídia (imagens dos livros)
├── templates/          # Templates globais
├── manage.py          # Script de gerenciamento do Django
├── requirements.txt   # Dependências do projeto
└── README.md         # Este arquivo
```

## 🔧 Configuração do Ambiente

### Requisitos
- Python 3.12 ou superior
- pip (gerenciador de pacotes Python)
- Git

### Variáveis de Ambiente
Crie um arquivo `.env` na raiz do projeto com:
```
DEBUG=True
SECRET_KEY=sua-chave-secreta-aqui
```

## 👤 Autor

**Ryan Ditko**
- GitHub: [@ryanditko](https://github.com/ryanditko)

## 🤖 Desenvolvimento com IA

Este projeto foi desenvolvido com a assistência do Claude (Anthropic), demonstrando como a IA pode ser utilizada como uma ferramenta de aprendizado e desenvolvimento. O processo incluiu:
- Geração de código base
- Debugging assistido
- Melhorias de design
- Boas práticas de programação

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 🌟 Agradecimentos

- Claude (Anthropic) pela assistência no desenvolvimento
- Comunidade Django pela documentação e recursos
- Bootstrap pela framework de design

## 🤝 Contribuindo

Contribuições são sempre bem-vindas! Sinta-se à vontade para:
1. Fazer um fork do projeto
2. Criar uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abrir um Pull Request 