import random # Importa a biblioteca random, utilizada para gerar quantidades aleatórias no estoque dos produtos.

print("Bem vindo a loja PYMarket!")

# Define os produtos, preços e quantidade em estoque. 
produtos = [
    {"nome": "Arroz", "preco": 25.90, "quantidade": random.randint(0,10)},
    {"nome": "Feijão", "preco": 8.50, "quantidade": random.randint(0,10)},
    {"nome": "Leite", "preco": 4.50, "quantidade": random.randint(0,10)},
    {"nome": "Café", "preco": 14.20, "quantidade": random.randint(0,10)},
    {"nome": "Açúcar", "preco": 5.80, "quantidade": random.randint(0,10)},
    {"nome": "Óleo de Soja", "preco": 7.90, "quantidade": random.randint(0,10)},
    {"nome": "Macarrão", "preco": 4.20, "quantidade": random.randint(0,10)},
    {"nome": "Molho de Tomate", "preco": 3.50, "quantidade": random.randint(0,10)},
    {"nome": "Sal", "preco": 2.50, "quantidade": random.randint(0,10)},
    {"nome": "Farinha de Trigo", "preco": 5.00, "quantidade": random.randint(0,10)},
    {"nome": "Manteiga", "preco": 9.90, "quantidade": random.randint(0,10)},
    {"nome": "Queijo Mussarela", "preco": 38.00, "quantidade": random.randint(0,10)},
    {"nome": "Presunto", "preco": 32.00, "quantidade": random.randint(0,10)},
    {"nome": "Pão de Forma", "preco": 7.50, "quantidade": random.randint(0,10)},
    {"nome": "Ovos (Dúzia)", "preco": 12.00, "quantidade": random.randint(0,10)},
    {"nome": "Sabão em Pó", "preco": 18.50, "quantidade": random.randint(0,10)},
    {"nome": "Detergente", "preco": 2.20, "quantidade": random.randint(0,10)},
    {"nome": "Papel Higiênico", "preco": 19.90, "quantidade": random.randint(0,10)},
    {"nome": "Pasta de Dente", "preco": 4.80, "quantidade": random.randint(0,10)},
    {"nome": "Azeite de Oliva", "preco": 34.90, "quantidade": random.randint(0,10)}
]

# Armazena as vendas realizadas.
vendas = []

# Exibe o menu até o fechamento do caixa.
while True:
  print("\n===== MENU =====")
  print("1 - Registrar venda")
  print("2 - Fechar caixa")
  opcao_menu = input("O que deseja fazer? ")

  # Inicia uma nova venda e cria o carrinho.
  if opcao_menu == "1":
    produtos_carrinho = []

    # Exibe os produtos e recebe os pedidos.
    while True:
        print("\nProdutos disponíveis:")
        for produto in produtos:
            print(f'{produto["nome"]} - R$ {produto["preco"]:.2f} - Estoque: {produto["quantidade"]}')

        produto_nome = input("\nQual produto você deseja comprar? ").lower()
        produto_quantidade = int(input("Quantas unidades? "))
        produto_encontrado = False

        # Verifica o produto e a quantidade disponível.
        for produto in produtos:
            if produto_nome == produto["nome"].lower():
                produto_encontrado = True
                if produto_quantidade <= 0:
                    print("\nQuantidade inválida! Digite um número maior que zero.")
                elif produto["quantidade"] >= produto_quantidade:
                    produtos_carrinho.append({
                        "nome": produto["nome"],
                        "quantidade": produto_quantidade
                    })
                    produto["quantidade"] -= produto_quantidade
                    print("Produto adicionado ao carrinho.")
                else:
                    print(f"\nDesculpe, estoque insuficiente. Temos apenas {produto['quantidade']} em estoque.")
                break

        # Informa caso o produto não exista.
        if not produto_encontrado:
            print("\nEsse produto não existe em nossa loja.")

        # Verifica o limite de itens do carrinho.
        if len(produtos_carrinho) == 20:
            print("Limite de 20 itens atingido!")
            break

        # Pergunta se deseja continuar comprando.
        opcao_adicionar = input("Deseja adicionar outro produto? s/n ").lower()
        if opcao_adicionar == "n":
            break

    # Cancela a venda se o carrinho estiver vazio.
    if len(produtos_carrinho) == 0:
        print("Nenhum produto foi adicionado. Venda cancelada.")
        continue

    # Calcula o subtotal e exibe o resumo da compra.
    subtotal = 0
    print("\nResumo Da Compra:")

    for item in produtos_carrinho:
        for produto in produtos:
            if produto["nome"] == item["nome"]:
                subtotal_produto = produto["preco"] * item["quantidade"]
                subtotal += subtotal_produto

                print(f'{item["nome"]} - {item["quantidade"]} unidades x R$ {produto["preco"]:.2f} = R$ {subtotal_produto:.2f}')
                break

    print(f"\nSubtotal: R$ {subtotal:.2f}")

    # Solicita e valida a forma de pagamento.
    while True:
        print("\nQual a forma de pagamento? (Selecione o dígito)")
        opcao_pagamento = input("1 - Dinheiro, 2 - Pix, 3 - Cartão \n")

        if opcao_pagamento == "1":
            forma_pagamento = "dinheiro"
            break
        elif opcao_pagamento == "2":
            forma_pagamento = "pix"
            break
        elif opcao_pagamento == "3":
            forma_pagamento = "cartao"
            break
        else:
            print("Opção inválida! Digite 1, 2 ou 3.")

    # Aplica descontos para pagamentos em dinheiro ou Pix.
    desconto = 0

    if forma_pagamento == "dinheiro" or forma_pagamento == "pix":
        if subtotal >= 200:
            desconto = subtotal * 0.10
        elif subtotal >= 100:
            desconto = subtotal * 0.05

    # Calcula e exibe o valor final da compra.
    valor_final = subtotal - desconto

    print(f"Desconto: R$ {desconto:.2f}")
    print(f"Valor final: R$ {valor_final:.2f}")

    # Verifica o valor recebido e calcula o troco.
    troco = 0
    valor_recebido = None

    if forma_pagamento == "dinheiro":
        while True:
            valor_recebido = float(input("Valor recebido: R$ "))

            if valor_recebido >= valor_final:
                troco = valor_recebido - valor_final
                break

            print("Valor insuficiente! Tente novamente.")

        print(f"Troco: R$ {troco:.2f}")

    # Registra os dados da venda concluída.
    vendas.append({
        # O ".copy()" cria uma cópia do carrinho, garantindo que os produtos da venda sejam salvos sem serem alterados por mudanças na lista original.
        "produtos": produtos_carrinho.copy(),
        "subtotal": subtotal,
        "desconto": desconto,
        "valor_final": valor_final,
        "pagamento": forma_pagamento,
        "valor_recebido": valor_recebido,
        "troco": troco
    })

    print("\nVenda concluída!")

  # Encerra o menu ou informa uma opção inválida.
  elif opcao_menu == "2":
      break
  else:
      print("Opção inválida! Digite 1 ou 2.")

# Inicializa os indicadores do fechamento do caixa.
quantidade_vendas = len(vendas)
faturamento = 0
maior_venda = 0
qtd_dinheiro = 0
qtd_pix = 0
qtd_cartao = 0

# Calcula o faturamento, a maior venda e os tipos de pagamento.
for venda in vendas:
    faturamento += venda["valor_final"]

    if venda["valor_final"] > maior_venda:
        maior_venda = venda["valor_final"]

    if venda["pagamento"] == "dinheiro":
        qtd_dinheiro += 1
    elif venda["pagamento"] == "pix":
        qtd_pix += 1
    else:
        qtd_cartao += 1

# Calcula o ticket médio das vendas.
if quantidade_vendas > 0:
    ticket_medio = faturamento / quantidade_vendas
else:
    ticket_medio = 0

# Exibe o relatório final do caixa.
print("\n===== FECHAMENTO DO CAIXA =====")
print(f"Quantidade de vendas: {quantidade_vendas}")
print(f"Faturamento: R$ {faturamento:.2f}")
print(f"Ticket médio: R$ {ticket_medio:.2f}")
print(f"Maior venda: R$ {maior_venda:.2f}")
print(f"Vendas em dinheiro: {qtd_dinheiro}")
print(f"Vendas no Pix: {qtd_pix}")
print(f"Vendas no cartão: {qtd_cartao}")