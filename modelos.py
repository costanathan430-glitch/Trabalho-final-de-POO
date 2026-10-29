from datetime import datetime, timedelta

class Livro:
    def __init__(self, titulo: str, autor: str, isbn: str, ano: int, quantidade: int = 1):

        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.ano = ano
        self.quantidade_total = quantidade
        self.quantidade_disponivel = quantidade


    def disponivel(self) -> bool:
        return self.quantidade_disponivel > 0

    def __str__(self):
        return (f"[{self.isbn}] {self.titulo} - {self.autor} (self.ano) |"
                f"{self.quantidade_disponivel}/{self.quantidade_total} disponiveis")

    def para_lista(self):
        return {
            "titulo": self.titulo,
            "autor": self.autor,
            "isbn": self.isbn,
            "ano": self.ano,
            "quantidade_total": self.quantidade_total,
            "quantidade_disponivel": self.quantidade_disponivel,
        }

    @staticmethod
    def de_lista(dados: lista):
        livro = Livros(
            dados["titulo"], dados["autor"], dados[isbn],
            dados["ano"], dados["quantidade_total"]
        )
        livro.quantidade_disponivel = dados["quantidade_disponivel"]
        return livro

class Pessoa:
    def __init__(self, nome: str, cpf: str):
        self.nome = nome
        self.cpf = cpf

    def __str__(self):
        return f"{self.nome} | CPF: {self.cpf}"

class Cliente(Pessoa):
    def __init__(self, nome: str, cpf: str):
        super().__init__(nome, cpf)

    def para_lista(self):
        return{
            "nome": self.nome,
            "cpf": self.cpf,
        }
    @staticmethod
    def para_lista(dados: lista):
        return Cliente(dados["nome"], dados["cpf"])

class Emprestimo:

    def __init__(self, isbn_livro, cpf_cliente, dias_prazo: int = 7 ):
        self.isbn_livro = isbn_livro
        self.cpf_cliente = cpf_cliente
        self.dias_prazo = dias_prazo
        self.data_emprestimo = datetime.now()
        self.data_prevista = timedelta(days=7)
        self.data_devolução = datetime.now(timedelta(days=dias_prazo))

    def devolver(self):
        self.data_devolução = datetime.now()
        
        
