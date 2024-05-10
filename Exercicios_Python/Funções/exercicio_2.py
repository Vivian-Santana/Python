'''
Suponha que você é um colecionar de jogos
de videogame. Escreva um algoritmo que
permita cadastrar esses jogos informando o
nome e a qual videogame ele pertence
Para isso, crie um menu de opções contendo:
cadastrar novo item, listar tudo que foi
cadastrado e sair

Para resolver esse exercício, crie pelo menos
uma função para cada item do menu
Além disso, armazene todos os dados em
um arquivo de texto que deve ser salvo em
disco e manter os dados cadastrados
'''
def cadastrar_jogo():
    nome = input("Digite o nome do jogo: ")
    videogame = input("Digite o nome do videogame: ")
    with open("jogos.txt", "a") as arquivo:
        arquivo.write(f"{nome},{videogame}\n")
    print("Jogo cadastrado com sucesso!")


def listar_jogos():
    try:
        with open("jogos.txt", "r") as arquivo:
            print("Jogos cadastrados:")
            for linha in arquivo:
                nome, videogame = linha.strip().split(",")
                print(f"Nome: {nome}, Videogame: {videogame}")
    except FileNotFoundError:
        print("Nenhum jogo cadastrado ainda.")


def menu():
    while True:
        print("\nMenu:")
        print("1. Cadastrar novo jogo")
        print("2. Listar todos os jogos cadastrados")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            cadastrar_jogo()
        elif opcao == "2":
            listar_jogos()
        elif opcao == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Escolha uma opção válida.")


if __name__ == "__main__":
    menu()
