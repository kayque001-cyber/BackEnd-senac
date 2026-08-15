import random


"""=== JOGADOR ==="""

jogador = {

    "nome": "Herói",
    "vida": 100,
    "vida_maxima": 100,
    "ataque": 25,
    "defesa": 10,
    "nivel": 1,
    "xp": 0,
    "xp_proximo": 100,
    "moedas": 50,
    "pocoes": 2
}


"""=== INVENTÁRIO ==="""

inventario = {
    "Poção": 2
}


"""=== INIMIGOS ==="""

inimigos = [

    {
        "nome": "Goblin",
        "vida": 50,
        "vida_maxima": 50,
        "ataque": 15,
        "defesa": 5,
        "xp": 50,
        "moedas": 20
    },

    {
        "nome": "Orc",
        "vida": 80,
        "vida_maxima": 80,
        "ataque": 20,
        "defesa": 8,
        "xp": 75,
        "moedas": 30
    },

    {
        "nome": "Cavaleiro",
        "vida": 120,
        "vida_maxima": 120,
        "ataque": 25,
        "defesa": 12,
        "xp": 100,
        "moedas": 50
    },

    {
        "nome": "Dragão",
        "vida": 180,
        "vida_maxima": 180,
        "ataque": 35,
        "defesa": 15,
        "xp": 200,
        "moedas": 100
    }
]


"""=== CALCULAR DANO ==="""

def calcular_dano(ataque, defesa):

    dano = ataque - defesa

    if dano < 0:

        dano = 0

    return dano


"""=== ATAQUE ALEATÓRIO ==="""

def ataque_aleatorio(ataque):

    minimo = ataque - 5

    if minimo < 1:

        minimo = 1

    return random.randint(
        minimo,
        ataque
    )


"""=== ATACAR ==="""

def atacar(atacante, defensor):

    ataque = ataque_aleatorio(
        atacante["ataque"]
    )

    dano = calcular_dano(
        ataque,
        defensor["defesa"]
    )

    defensor["vida"] -= dano

    if defensor["vida"] < 0:

        defensor["vida"] = 0

    print(
        f'\n{atacante["nome"]} causou '
        f'{dano} de dano!'
    )

    print(
        f'{defensor["nome"]}: '
        f'{defensor["vida"]}/'
        f'{defensor["vida_maxima"]} HP'
    )


"""=== USAR POÇÃO ==="""

def usar_pocao():

    if jogador["pocoes"] <= 0:

        print(
            "\nVocê não possui poções!"
        )

        return

    if jogador["vida"] >= jogador["vida_maxima"]:

        print(
            "\nSua vida está cheia!"
        )

        return

    jogador["vida"] += 30

    if jogador["vida"] > jogador["vida_maxima"]:

        jogador["vida"] = jogador["vida_maxima"]

    jogador["pocoes"] -= 1

    inventario["Poção"] -= 1

    print(
        "\nVocê usou uma poção!"
    )

    print(
        f'Vida: {jogador["vida"]}/'
        f'{jogador["vida_maxima"]}'
    )


"""=== GANHAR XP ==="""

def ganhar_xp(quantidade):

    jogador["xp"] += quantidade

    print(
        f"\nVocê ganhou {quantidade} XP!"
    )

    verificar_nivel()


"""=== VERIFICAR NÍVEL ==="""

def verificar_nivel():

    if jogador["xp"] >= jogador["xp_proximo"]:

        jogador["xp"] -= jogador["xp_proximo"]

        jogador["nivel"] += 1

        jogador["xp_proximo"] += 50

        jogador["vida_maxima"] += 20

        jogador["vida"] = jogador["vida_maxima"]

        jogador["ataque"] += 5

        jogador["defesa"] += 2

        print(
            "\n===== LEVEL UP! ====="
        )

        print(
            f'Você chegou ao nível '
            f'{jogador["nivel"]}!'
        )

        print(
            f'Vida: {jogador["vida_maxima"]}'
        )

        print(
            f'Ataque: {jogador["ataque"]}'
        )

        print(
            f'Defesa: {jogador["defesa"]}'
        )


"""=== INVENTÁRIO ==="""

def mostrar_inventario():

    print("\n=== INVENTÁRIO ===")

    print(
        f'Poções: {jogador["pocoes"]}'
    )

    print(
        f'Moedas: {jogador["moedas"]}'
    )


"""=== STATUS ==="""

def mostrar_status():

    print("\n=== STATUS ===")

    print(
        f'Nome: {jogador["nome"]}'
    )

    print(
        f'Nível: {jogador["nivel"]}'
    )

    print(
        f'Vida: {jogador["vida"]}/'
        f'{jogador["vida_maxima"]}'
    )

    print(
        f'Ataque: {jogador["ataque"]}'
    )

    print(
        f'Defesa: {jogador["defesa"]}'
    )

    print(
        f'XP: {jogador["xp"]}/'
        f'{jogador["xp_proximo"]}'
    )

    print(
        f'Moedas: {jogador["moedas"]}'
    )

    print(
        f'Poções: {jogador["pocoes"]}'
    )


"""=== COMBATE ==="""

def combate(inimigo):

    inimigo = inimigo.copy()

    print(
        f'\n{inimigo["nome"]} apareceu!'
    )

    while (
        jogador["vida"] > 0
        and
        inimigo["vida"] > 0
    ):

        print("\n=== SEU TURNO ===")

        print("1 - Atacar")
        print("2 - Usar poção")
        print("3 - Status")
        print("4 - Inventário")

        opcao = input(
            "\nEscolha: "
        )

        if opcao == "1":

            atacar(
                jogador,
                inimigo
            )

        elif opcao == "2":

            usar_pocao()

            continue

        elif opcao == "3":

            mostrar_status()

            continue

        elif opcao == "4":

            mostrar_inventario()

            continue

        else:

            print(
                "Opção inválida!"
            )

            continue

        if inimigo["vida"] <= 0:

            print(
                f'\n{inimigo["nome"]} foi derrotado!'
            )

            jogador["moedas"] += inimigo["moedas"]

            print(
                f'Você ganhou '
                f'{inimigo["moedas"]} moedas!'
            )

            ganhar_xp(
                inimigo["xp"]
            )

            return True

        print("\n=== TURNO DO INIMIGO ===")

        atacar(
            inimigo,
            jogador
        )

        if jogador["vida"] <= 0:

            print(
                "\nVocê foi derrotado!"
            )

            return False


"""=== INICIAR FASE ==="""

def iniciar_fase(numero_fase):

    inimigo = inimigos[
        numero_fase - 1
    ]

    print(
        f"\n===== FASE {numero_fase} ====="
    )

    venceu = combate(inimigo)

    return venceu


"""=== INICIAR AVENTURA ==="""

def iniciar_aventura():

    fase = 1

    print(
        "\n===== AVENTURA RPG ====="
    )

    while fase <= len(inimigos):

        venceu = iniciar_fase(fase)

        if venceu == False:

            print(
                "\n===== GAME OVER ====="
            )

            break

        if fase == len(inimigos):

            print(
                "\n===== PARABÉNS! ====="
            )

            print(
                "Você completou todas as fases!"
            )

            mostrar_status()

            break

        fase += 1

        print(
            f"\nFase {fase} desbloqueada!"
        )

        jogador["vida"] += 20

        if jogador["vida"] > jogador["vida_maxima"]:

            jogador["vida"] = jogador["vida_maxima"]


iniciar_aventura()