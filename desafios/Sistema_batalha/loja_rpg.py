"""=== PRODUTOS ==="""

produtos = [

    {
        "nome": "Glock",
        "preco": 100,
        "categoria": "Arma",
        "desconto": 0,
        "lendario": False
    },

    {
        "nome": "M500",
        "preco": 200,
        "categoria": "Arma",
        "desconto": 10,
        "lendario": False
    },

    {
        "nome": "Desert",
        "preco": 300,
        "categoria": "Arma",
        "desconto": 0,
        "lendario": False
    },

    {
        "nome": "Excalibur",
        "preco": 1000,
        "categoria": "Arma",
        "desconto": 20,
        "lendario": True
    }
]


"""=== INVENTÁRIO ==="""

inventario = {}


"""=== VISUALIZAR PRODUTOS ==="""

def visualizar_produtos(produtos):

    print("\n=== PRODUTOS DISPONÍVEIS ===")

    for i, produto in enumerate(produtos, start=1):

        preco = produto["preco"]

        desconto = produto["desconto"]

        preco_final = (
            preco - (preco * desconto / 100)
        )

        print(
            f'\n{i} - {produto["nome"]}'
        )

        print(
            f'Categoria: {produto["categoria"]}'
        )

        print(
            f'Preço: R$ {preco_final:.2f}'
        )

        if desconto > 0:

            print(
                f'Desconto: {desconto}%'
            )

        if produto["lendario"]:

            print(
                "ITEM LENDÁRIO!"
            )


"""=== COMPRAR ==="""

def comprar(produtos, saldo):

    visualizar_produtos(produtos)

    produto_selecionado = int(
        input(
            "\nQual produto deseja comprar?: "
        )
    )

    if (
        produto_selecionado < 1
        or
        produto_selecionado > len(produtos)
    ):

        print("Produto inexistente!")

        return saldo

    indice = produto_selecionado - 1

    produto = produtos[indice]

    preco = produto["preco"]

    desconto = produto["desconto"]

    preco_final = (
        preco - (preco * desconto / 100)
    )

    print(
        f'\nVocê escolheu: '
        f'{produto["nome"]}'
    )

    print(
        f'Preço: R$ {preco_final:.2f}'
    )

    quantidade = int(
        input("Quantidade: ")
    )

    if quantidade <= 0:

        print("Quantidade inválida!")

        return saldo

    total = preco_final * quantidade

    if saldo < total:

        print("Saldo insuficiente!")

        return saldo

    saldo -= total

    if produto["nome"] in inventario:

        inventario[
            produto["nome"]
        ] += quantidade

    else:

        inventario[
            produto["nome"]
        ] = quantidade

    print("\nCompra realizada!")

    print(
        f"Total: R$ {total:.2f}"
    )

    print(
        f"Saldo: R$ {saldo:.2f}"
    )

    return saldo


"""=== INVENTÁRIO ==="""

def visualizar_inventario():

    print("\n=== INVENTÁRIO ===")

    if not inventario:

        print("Inventário vazio!")

        return

    for nome, quantidade in inventario.items():

        print(
            f"{nome} | Quantidade: {quantidade}"
        )


"""=== VENDER ==="""

def vender(produtos, saldo):

    visualizar_inventario()

    if not inventario:

        return saldo

    nome_item = input(
        "\nQual item deseja vender?: "
    )

    if nome_item not in inventario:

        print(
            "Você não possui esse item!"
        )

        return saldo

    quantidade = int(
        input("Quantidade: ")
    )

    if quantidade <= 0:

        print("Quantidade inválida!")

        return saldo

    if quantidade > inventario[nome_item]:

        print(
            "Você não possui essa quantidade!"
        )

        return saldo

    produto_encontrado = None

    for produto in produtos:

        if (
            produto["nome"].lower()
            ==
            nome_item.lower()
        ):

            produto_encontrado = produto

            break

    if produto_encontrado is None:

        print("Produto não encontrado!")

        return saldo

    preco_venda = (
        produto_encontrado["preco"] * 0.5
    )

    total = preco_venda * quantidade

    inventario[nome_item] -= quantidade

    if inventario[nome_item] == 0:

        del inventario[nome_item]

    saldo += total

    print("\nVenda realizada!")

    print(
        f"Você recebeu: R$ {total:.2f}"
    )

    print(
        f"Saldo: R$ {saldo:.2f}"
    )

    return saldo


"""=== CARTEIRA ==="""

def carteira(saldo):

    print("\n=== CARTEIRA ===")

    print(
        f"Saldo: R$ {saldo:.2f}"
    )


"""=== LOJA ==="""

def loja_ativa():

    saldo = 500

    while True:

        print("\n=== LOJA DE RPG ===")

        print("1 - Produtos")
        print("2 - Comprar")
        print("3 - Inventário")
        print("4 - Vender")
        print("5 - Saldo")
        print("6 - Sair")

        opcao = int(
            input("\nEscolha: ")
        )

        match opcao:

            case 1:

                visualizar_produtos(
                    produtos
                )

            case 2:

                saldo = comprar(
                    produtos,
                    saldo
                )

            case 3:

                visualizar_inventario()

            case 4:

                saldo = vender(
                    produtos,
                    saldo
                )

            case 5:

                carteira(saldo)

            case 6:

                print(
                    "Obrigado por visitar a loja!"
                )

                break

            case _:

                print(
                    "Opção inválida!"
                )


loja_ativa()