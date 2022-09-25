from random import randint

print("Pedra, papel e tesoura!")
while True:
    print("Você que jogar?")
    confirmar = input("Digite (S) para sim e (N) para não: ")

    while confirmar == "s" or confirmar == "S":
        print("para jogar só um jogador digite (1) e para jogar dois jogadores digite (2).")
        jogadores = input("Digite o número de jogadores: ")

        if jogadores == "1":
            nome = input("Digite o seu nome jogador: ")

            print("Ecolha (0) para pedra, (1) para papel e (2) para tesoura.")
            jogador = input(f"{nome} coloque o número escolhido: ")

            computador = randint(0, 2)

            if jogador == "0" and computador == 0:
                print(f"{nome} escolheu pedra e computador escolheu pedra!")
                print("Empate!")
            elif jogador == "0" and computador == 1:
                print(f"{nome} escolheu pedra e computador escolheu papel!")
                print("Computador ganhou!")
            elif jogador == "0" and computador == 2:
                print(f"{nome} escolheu pedra e computador escolheu tesoura!")
                print(f"{nome} ganhou!")
            elif jogador == "1" and computador == 0:
                print(f"{nome} escolheu papel e computador escolheu pedra!")
                print(f"{nome} ganhou!")
            elif jogador == "1" and computador == 1:
                print(f"{nome} escolheu papel e computador escolheu papel!")
                print("Empate!")
            elif jogador == "1" and computador == 2:
                print(f"{nome} escolheu papel e computador escolheu tesoura!")
                print("Computador ganhou!")
            elif jogador == "2" and computador == 0:
                print(f"{nome} escolheu tesoura e computador escolheu pedra!")
                print("computador ganhou!")
            elif jogador == "2" and computador == 1:
                print(f"{nome} escolheu tesoura e computador escolheu papel!")
                print(f"{nome} ganhou!")
            elif jogador == "2" and computador == 2:
                print(f"{nome} escolheu tesoura e computador escolheu tesoura!")
                print("Empate!")
            else:
                print(f"{nome} coloque um valor valido!")
        elif jogadores == "2":
            nome_1 = input("Digite o seu nome jogador 1: ")
            nome_2 = input("Digite o seu nome jogador 2: ")

            print("Ecolha (0) para pedra, (1) para papel e (2) para tesoura.")
            jogador_1 = input(f"{nome_1} coloque o número escolhido: ")
            jogador_2 = input(f"{nome_2} coloque o número escolhido: ")

            if jogador_1 == "0" and jogador_2 == "0":
                print(f"{nome_1} escolheu pedra e {nome_2} escolheu pedra!")
                print("Empate!")
            elif jogador_1 == "0" and jogador_2 == "1":
                print(f"{nome_1} escolheu pedra e {nome_2} escolheu papel!")
                print(f"{nome_2} ganhou!")
            elif jogador_1 == "0" and jogador_2 == "2":
                print(f"{nome_1} escolheu pedra e {nome_2} escolheu tesoura!")
                print(f"{nome_1} ganhou!")
            elif jogador_1 == "1" and jogador_2 == "0":
                print(f"{nome_1} escolheu papel e {nome_2} escolheu pedra!")
                print(f"{nome_1} ganhou!")
            elif jogador_1 == "1" and jogador_2 == "1":
                print(f"{nome_1} escolheu papel e {nome_2} escolheu papel!")
                print("Empate!")
            elif jogador_1 == "1" and jogador_2 == "2":
                print(f"{nome_1} escolheu papel e {nome_2} escolheu tesoura!")
                print(f"{nome_2} ganhou!")
            elif jogador_1 == "2" and jogador_2 == "0":
                print(f"{nome_1} escolheu tesoura e {nome_2} escolheu pedra!")
                print(f"{nome_2} ganhou!")
            elif jogador_1 == "2" and jogador_2 == "1":
                print(f"{nome_1} escolheu tesoura e {nome_2} escolheu papel!")
                print(f"{nome_1} ganhou!")
            elif jogador_1 == "2" and jogador_2 == "2":
                print(f"{nome_1} escolheu tesoura e {nome_2} escolheu tesoura!")
                print("Empate!")
            else:
                print("Coloque um valor valido!")
        else:
            print("Coloque um valor valido!")

        print("Você que jogar?")
        confirmar = input("Digite (S) para sim e (N) para não: ")
    if confirmar == "n" or confirmar == "N":
        print("Jogo encerrado!")
        break
    else:
        print("Coloque um valor valido!")
