import random

from modelos import Livro

def criar_acervo_inicial() -> list[Livro]:

    dados = [
        ("Dom Casmurro", "Machado de Assis", "00", 1899),
        ("E Não sobrou nenhum", "Agatha Christie", "01", 1939),
        ("Um Estudo de Vermelho", "Sir Arthut Conan Doyle", "02", 1887),
        ("Dom Quixote", "Miguel de Cervantes", "03", 1605),
        ("Jantar Secreto", "Raphael Montes", "04", 2016),
        ("Sagarana", "Joao Guimaraes Rosa", "05", 1946),
        ("Hamlet", "William Shakespeare", "06", 1600),
        ("Sao Bernardo", "Graciliano Ramos", "07", 1934),
        ("Harry Potter e a Pedra Filosofal", "J.K. Rowling", "08", 1997),
        ("Gabriela, Cravo e Canela", "Jorge Amado", "09", 1958),
        ("O Cortico", "Aluisio Azevedo", "10", 1890),
        ("Verity", "Collen Hoover", "11", 2018),
        ("A Paixao Segundo G.H.", "Clarice Lispector", "12", 1964),
        ("Macunaima", "Mario de Andrade", "13", 1928),
        ("O Ateneu", "Raul Pompeia", "14", 1888),
        ("Os Sertoes", "Euclides da Cunha", "15", 1902),
        ("Triste Fim de Policarpo Quaresma", "Lima Barreto", "16", 1915),
        ("A Hipótese do Amor", "Ali Hazelwood", "17", 2026),
        ("A Culpa é das Estrelas", "John Green", "18", 2012),
        ("O Guarani", "Jose de Alencar", "19", 1857),
    ]

    acervo = []
    for titulo, autor, isbn, ano in dados:
        quantidade = random.randint(1,9)
        acervo.append(Livro(titulo, autor, isbn, ano, quantidade))
    return acervo
