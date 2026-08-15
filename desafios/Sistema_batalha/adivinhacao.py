import random


def iniciar_jogo():

    tentativas = 0
    total_tentativas = 7

    pontuacao = [
        100,
        80,
        60,
        40,
        20,
        10,
        5
    ]

    numero_aleatorio = random.randint(1, 100)

    while tentativas < total_tentativas:

        print(
            "\n==== ADIVINHE O NÚMERO ESCOLHIDO ====\n"
        )

        resposta = int(
            input("Qual é o número?: ")
        )

        tentativas += 1

        tentativas_restantes = (
            total_tentativas - tentativas
        )

        if resposta == numero_aleatorio:

            pontos = pontuacao[tentativas - 1]

            print(
                "\nParabéns! Você acertou!!"
            )

            print(
                f"Você acertou na "
                f"{tentativas}ª tentativa!"
            )

            print(
                f"Você ganhou {pontos} pontos!"
            )

            break

        elif resposta > numero_aleatorio:

            print(
                "O número é menor!"
            )

            print(
                "Tente novamente!"
            )

        elif resposta < numero_aleatorio:

            print(
                "O número é maior!"
            )

            print(
                "Tente novamente!"
            )

        print(
            f"Tentativas restantes: "
            f"{tentativas_restantes}"
        )

    else:

        print("\n=== FIM DE JOGO ===")

        print(
            "Tentativas expiradas!"
        )

        print(
            "Você perdeu!"
        )

        print(
            f"O número era: "
            f"{numero_aleatorio}"
        )


iniciar_jogo()