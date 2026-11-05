from biblioteca import Biblioteca
#chamo criar_acervo_inicial e salvo em uma variavel
from acervo import criar_acervo_inicial

acervos = criar_acervo_inicial()
 
 #criar funcao pra digitar a data para o sistema
 
while True:
    print("\n BIBLIOTECA \n")
    print("Ver acervo (1) ")
    print("Cadastrar usuario (2) ")
    print("Pegar emprestado (3) ")
    print("Devolver livro (4) ")
    print("Ver livros em atraso (5) ")
    print("Ver livros emprestados (6) ")
    print("Sair do sistema (7) ")

    try:
        opcao = int(input("Escolha uma opcao: "))
        if opcao == 1:
            print(acervos)
         #print dos livros
         
        elif opcao == 2:
            nome = imput ("digite seu usuario: ")
        #puxa a biblioteca para cadastrar o usuario


        elif opcao == 3:
            nome = input("Usuario: ")
            livro = input("Livro desejado: ")
        # puxa o usuario e busca o livro e guarda no emprestado

        elif opcao == 4:
            nome = input("Usuario:")
            livro = input("Livro pra devolver")
        #puxa o usuario e o livro que tem emprestado e devolve

        elif opcao == 5:
            nome = input("Usuario:")
        #puxa o nome do usuario e seus livros em atraso só mostra os livros

        elif opcao == 6:
            nome = input("Usuario:")
        #chama os emprestimos do usuario só mostra os livros e data de vencimento

        elif opcao == 7:
            print("fechando")
            break

        else:
            printf("opcao invalida")

    except ValueError:
        print("Erro: digite uma opcao")

            #pesquisar com busca parcial