import random

from modelos import Livro

def criar_acervo_inicial() -> list[Livro]:

    dados = [
        ("Dom Casmurro", "Machado de Assis", "00", 1899),
        ("Memorias Postumas de Bras Cubas", "Machado de Assis", "01", 1881),
        ("Quincas Borba", "Machado de Assis", "02", 1891),
        ("Helena", "Machado de Assis", "03", 1876),
        ("Grande Sertao: Veredas", "Joao Guimaraes Rosa", "04", 1956),
        ("Sagarana", "Joao Guimaraes Rosa", "05", 1946),
        ("Vidas Secas", "Graciliano Ramos", "06", 1938),
        ("Sao Bernardo", "Graciliano Ramos", "07", 1934),
        ("Capitaes da Areia", "Jorge Amado", "08", 1937),
        ("Gabriela, Cravo e Canela", "Jorge Amado", "09", 1958),
        ("O Cortico", "Aluisio Azevedo", "10", 1890),
        ("A Hora da Estrela", "Clarice Lispector", "11", 1977),
        ("A Paixao Segundo G.H.", "Clarice Lispector", "12", 1964),
        ("Macunaima", "Mario de Andrade", "13", 1928),
        ("O Ateneu", "Raul Pompeia", "14", 1888),
        ("Os Sertoes", "Euclides da Cunha", "15", 1902),
        ("Triste Fim de Policarpo Quaresma", "Lima Barreto", "16", 1915),
        ("Fogo Morto", "Jose Lins do Rego", "17", 1943),
        ("Iracema", "Jose de Alencar", "18", 1865),
        ("O Guarani", "Jose de Alencar", "19", 1857),
    ]

    acervo = []
    for titulo, autor, isbn, ano in dados:
        quantidade = random.randint(1,9)
        acervo.append(Livro(titulo, autor, isbn, ano, quantidade))
    return acervo
