import random


def iniciar_jogo():
    tentativas = 0
    total_tentativas = 6
    pontuacao = [100, 80, 60, 40, 20, 10]
    numero_aleatorio = random.randint(1, 100)
    while tentativas <= total_tentativas:
        nova_tentativa = total_tentativas - tentativas
        if tentativas >= 7:
            print("Tentativas expiradas!"
                  "Você Perdeu!"
                )
            break
        print("\n====ADIVINHE O NÚMERO ESCOLHIDO====\n")
    
        resposta = int(input("Qual é o Número?: "))
        if resposta == numero_aleatorio:
            print("Parabéns você Acertou!!")
            match tentativas:
                case 1:
                    print(f"Você ganhou {pontuacao[0]} nessa tentativa! ")
                case 2:
                    print(f"Você ganhou {pontuacao[1]} nessa tentativa! ")
                case 3:
                    print(f"Você ganhou {pontuacao[2]} nessa tentativa! ")
                case 4:
                    print(f"Você ganhou {pontuacao[3]} nessa tentativa! ")
                case 5:
                    print(f"Você ganhou {pontuacao[4]} nessa tentativa! ")
                case 6:
                    print(f"Você ganhou {pontuacao[5]} nessa tentativa! ")

            break
        elif resposta > numero_aleatorio:
            print("O Número è Menor!\n"
                  "Tente novamente!"
                )
            tentativas = tentativas +1
            print(f"Tentativas restantes: {nova_tentativa}")
        elif resposta < numero_aleatorio:
            print("O Número è Maior!\n"
                "Tente novamente!"
            )
            tentativas = tentativas +1
            print(f"Tentativas restantes: {nova_tentativa}")
        

iniciar_jogo()
                        