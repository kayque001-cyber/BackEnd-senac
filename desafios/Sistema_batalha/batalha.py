import random


"""=== CALCULAR DANO ==="""

def calcular_dano(ataque, defesa):

    dano = ataque - defesa

    if dano < 0:
        dano = 0

    return dano


"""=== ATAQUE ALEATÓRIO ==="""

def ataque_aleatorio(ataque):

    minimo = ataque - 10

    if minimo < 1:
        minimo = 1

    dano_aleatorio = random.randint(minimo, ataque)

    return dano_aleatorio


"""=== ATAQUE CRÍTICO ==="""

def ataque_critico(dano):

    numero_sorteado = random.randint(1, 100)

    if numero_sorteado <= 20:

        dano = dano * 2

        print("ATAQUE CRÍTICO!!!")

    return dano


"""=== CHANCE DE ESQUIVA ==="""

def chance_esquiva(defensor):

    numero_sorteado = random.randint(1, 100)

    if numero_sorteado <= defensor["esquiva"]:

        print(
            f'{defensor["nome"]} conseguiu esquivar!'
        )

        return True

    return False


"""=== ATACAR ==="""

def atacar(atacante, defensor):

    if chance_esquiva(defensor):

        return

    ataque_sorteado = ataque_aleatorio(
        atacante["ataque"]
    )

    dano = calcular_dano(
        ataque_sorteado,
        defensor["defesa"]
    )

    dano = ataque_critico(dano)

    nova_vida = defensor["vida"] - dano

    if nova_vida < 0:

        nova_vida = 0

    defensor["vida"] = nova_vida

    print(
        f'{atacante["nome"]} causou '
        f'{dano} de dano em '
        f'{defensor["nome"]}'
    )

    print(
        f'{defensor["nome"]} está com '
        f'{defensor["vida"]} de vida!'
    )

    if defensor["vida"] == 0:

        print(
            f'{defensor["nome"]} morreu!'
        )


"""=== CURAR ==="""

def curar(personagem):

    vida = personagem["vida"]
    vida_maxima = personagem["vida_maxima"]

    if personagem["pocoes"] <= 0:

        return

    if vida <= 40:

        print("\n=== POÇÃO DE CURA ===")

        print("1 - Usar poção")
        print("2 - Não usar")

        opcao = int(
            input("Escolha: ")
        )

        if opcao == 1:

            vida += 30

            if vida > vida_maxima:

                vida = vida_maxima

            personagem["vida"] = vida

            personagem["pocoes"] -= 1

            print("Poção utilizada!")

            print(
                f'Vida: {personagem["vida"]}/'
                f'{vida_maxima}'
            )

        elif opcao == 2:

            print("Você não usou a poção.")


"""=== BATALHA ==="""

def batalha():

    while True:

        print("\n=== TURNO DO HERÓI ===")

        curar(jogador)

        atacar(
            jogador,
            inimigo
        )

        if inimigo["vida"] <= 0:

            print("\nVitória do Herói!")

            break

        print("\n=== TURNO DO INIMIGO ===")

        atacar(
            inimigo,
            jogador
        )

        if jogador["vida"] <= 0:

            print("\nVitória do inimigo!")

            break


"""=== PERSONAGENS ==="""

jogador = {

    "nome": "Herói",
    "vida": 100,
    "vida_maxima": 100,
    "defesa": 20,
    "ataque": 30,
    "pocoes": 1,
    "esquiva": 20
}


inimigo = {

    "nome": "Vilão",
    "vida": 150,
    "vida_maxima": 150,
    "defesa": 10,
    "ataque": 30,
    "pocoes": 0,
    "esquiva": 10
}


batalha()