'''=== Calcular o Dano ==='''

def calcular_dano(ataque, defesa):
    dano = ataque - defesa
    if dano < 0:
        dano = 0
    return dano



'''=== Ataques ==='''

def atacar(atacante, defensor):
    ataque_sorteado = ataque_aleatorio(atacante["ataque"])
    dano = calcular_dano(ataque_sorteado, defensor["defesa"])
    dano = ataque_critico(dano)
    nova_vida = defensor["vida"] - dano
    if nova_vida <0:
        nova_vida = 0
    

    print(f'{atacante["nome"]} causou {dano} de dano em {defensor["nome"]}')
    print(f'{defensor["nome"]} estar com {defensor["vida"]} de vida!')
    if nova_vida == 0:
        print(f'{defensor["nome"]} Morreu!')
    defensor["vida"] = nova_vida

    
def ataque_aleatorio(ataque):
    import random
    minimo = ataque - 10
    dano_aleatorio = random.randint(minimo, ataque)
    
    return dano_aleatorio



def ataque_critico(dano):
    import random
    numero_sorteado = random.randint(1, 100)
    if numero_sorteado <= 20:
        dano = dano *2
        print(f"Ataque CRITÍCO!!!")
    return dano


'''====CURAR==='''
def curar(personagem):
    vida = personagem["vida"]
    maximo_vida = personagem["vida_maxima"]
    pocao = personagem["pocoes"]

    if pocao >= 1:
        if vida <= 40:
            print("Deseja curar seu Personagem agora?")
            print("1- Sim\n"
                    "2- Não"
                )
            opcao = int(input("Digite o alternativa numérica: "))
            if opcao == 1:
                vida = vida + 30
                pocao = personagem["pocoes"] - 1
                personagem["pocoes"] = pocao
            elif opcao == 2:
                return vida
        1
        if vida > maximo_vida:
            vida = maximo_vida
        
        personagem["vida"] = vida
        return personagem["vida"]
         

    



'''===BATALHA==='''

def batalha():
    while True:
        print("\n===Turno do Herói===")
        curar(jogador)
        atacar(jogador, inimigo)
        if inimigo["vida"] <= 0:
                    print("Vitória do Herói")
                    break
        print("\n===Turno do Inimigo===")
        atacar(inimigo, jogador)
        if jogador["vida"] <= 0:
            print("Vitória do inimigo")
            break
        

'''=== Personagens ==='''

jogador ={
    "nome" : "Herói",
    "vida" : 100,
    "vida_maxima": 100,
    "defesa" : 20,
    "ataque" : 30,
    "pocoes" : 1
}

inimigo ={
    "nome" : "Vilão",
    "vida" : 150,
    "vida_maxima": 150,
    "defesa" : 10,
    "ataque" : 30
}


batalha()