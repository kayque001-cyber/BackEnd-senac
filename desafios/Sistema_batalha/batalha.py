import random



'''===Função de Cálculo de Dano=== '''
def calcular_dano(ataque, defesa):
    ataque_aleatorio = random.randint(ataque - 5, ataque + 10)

    dano = ataque_aleatorio - defesa

    if dano <= 0:
        dano = 0

    return dano




'''===Função de Ataque=== '''
def atacar(atacante,defensor):
    dano = calcular_dano(atacante["ataque"], defensor["defesa"])

    defensor["vida"] -=dano

    

    print(
        f'{atacante["nome"]} atacou ' 
        f'{defensor["nome"]} causando {dano} de dano'
    )
    print(
        f'vida de {defensor["nome"]}:'
        f'{defensor["vida"]}'
    )
    if defensor["vida"]<=10:
        defensor["vida"] += curar(personagem=defensor)
        print(f'\n{defensor["nome"]} recuperou {curar(personagem=defensor)} de vida!')
    if defensor["vida"]<=0:
        defensor["vida"]=0



'''===Função de Cura=== '''
def curar(personagem):
    cura = random.randint(1, 30)
    return cura



jogador = {
    "nome":"Thor",
    "vida": 100,
    "ataque": 30,
    "defesa": 15
}

inimigo = {
    "nome":"Slime",
    "vida": 100,
    "ataque": 30,
    "defesa": 15
}




print("======BATALHA=====")
while jogador["vida"]>0 and inimigo["vida"]>0:
    print("\n ---Turno do Jogador---")
    atacar(jogador, inimigo)
    if inimigo["vida"]<=0:
        print("\n 🏆Vitória do Jogador!!")
        break
    print("\n ---Turno do Inimigo---")
    atacar(inimigo, jogador)
    if jogador["vida"]<=0:
        print("\n Você perdeu!!")
        break