import random # Fun;áo

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
  opcaoMenu = input("O que deseja fazer? ")

  # Inicia uma nova venda e cria o carrinho.
  if opcaoMenu == "1":
    produtosCarrinho = []

    # Exibe os produtos e recebe os pedidos.
    while True:
        print("\nProdutos disponíveis:")
        for produto in produtos:
            print(f'{produto["nome"]} - R$ {produto["preco"]:.2f} - Estoque: {produto["quantidade"]}')

        produtoNome = input("\nQual produto você deseja comprar? ").lower()
        produtoQuantidade = int(input("Quantas unidades? "))
        produtoEncontrado = False

        # Verifica o produto e a quantidade disponível.
        for produto in produtos:
            if produtoNome == produto["nome"].lower():
                produtoEncontrado = True
                if produtoQuantidade <= 0:
                    print("\nQuantidade inválida! Digite um número maior que zero.")
                elif produto["quantidade"] >= produtoQuantidade:
                    produtosCarrinho.append({
                        "nome": produto["nome"],
                        "quantidade": produtoQuantidade
                    })
                    produto["quantidade"] -= produtoQuantidade
                    print("Produto adicionado ao carrinho.")
                else:
                    print(f"\nDesculpe, estoque insuficiente. Temos apenas {produto['quantidade']} em estoque.")
                break

        # Informa caso o produto não exista.
        if not produtoEncontrado:
            print("\nEsse produto não existe em nossa loja.")

        # Verifica o limite de itens do carrinho.
        if len(produtosCarrinho) == 20:
            print("Limite de 20 itens atingido!")
            break

        # Pergunta se deseja continuar comprando.
        opcaoAdicionar = input("Deseja adicionar outro produto? s/n ").lower()
        if opcaoAdicionar == "n":
            break

    # Cancela a venda se o carrinho estiver vazio.
    if len(produtosCarrinho) == 0:
        print("Nenhum produto foi adicionado. Venda cancelada.")
        continue

    # Calcula o subtotal e exibe o resumo da compra.
    subtotal = 0
    print("\nResumo Da Compra:")

    for item in produtosCarrinho:
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
        opcaoPagamento = input("1 - Dinheiro, 2 - Pix, 3 - Cartão \n")

        if opcaoPagamento == "1":
            formaPagamento = "dinheiro"
            break
        elif opcaoPagamento == "2":
            formaPagamento = "pix"
            break
        elif opcaoPagamento == "3":
            formaPagamento = "cartao"
            break
        else:
            print("Opção inválida! Digite 1, 2 ou 3.")

    # Aplica descontos para pagamentos em dinheiro ou Pix.
    desconto = 0

    if formaPagamento == "dinheiro" or formaPagamento == "pix":
        if subtotal >= 200:
            desconto = subtotal * 0.10
        elif subtotal >= 100:
            desconto = subtotal * 0.05

    # Calcula e exibe o valor final da compra.
    valorFinal = subtotal - desconto

    print(f"Desconto: R$ {desconto:.2f}")
    print(f"Valor final: R$ {valorFinal:.2f}")

    # Verifica o valor recebido e calcula o troco.
    troco = 0
    valorRecebido = None

    if formaPagamento == "dinheiro":
        while True:
            valorRecebido = float(input("Valor recebido: R$ "))

            if valorRecebido >= valorFinal:
                troco = valorRecebido - valorFinal
                break

            print("Valor insuficiente! Tente novamente.")

        print(f"Troco: R$ {troco:.2f}")

    # Registra os dados da venda concluída.
    vendas.append({
        "produtos": produtosCarrinho.copy(),
        "subtotal": subtotal,
        "desconto": desconto,
        "valorFinal": valorFinal,
        "pagamento": formaPagamento,
        "valorRecebido": valorRecebido,
        "troco": troco
    })

    print("\nVenda concluída!")

  # Encerra o menu ou informa uma opção inválida.
  elif opcaoMenu == "2":
      break
  else:
      print("Opção inválida! Digite 1 ou 2.")

# Inicializa os indicadores do fechamento do caixa.
quantidadeVendas = len(vendas)
faturamento = 0
maiorVenda = 0
qtdDinheiro = 0
qtdPix = 0
qtdCartao = 0

# Calcula o faturamento, a maior venda e os tipos de pagamento.
for venda in vendas:
    faturamento += venda["valorFinal"]

    if venda["valorFinal"] > maiorVenda:
        maiorVenda = venda["valorFinal"]

    if venda["pagamento"] == "dinheiro":
        qtdDinheiro += 1
    elif venda["pagamento"] == "pix":
        qtdPix += 1
    else:
        qtdCartao += 1

# Calcula o ticket médio das vendas.
if quantidadeVendas > 0:
    ticketMedio = faturamento / quantidadeVendas
else:
    ticketMedio = 0

# Exibe o relatório final do caixa.
print("\n===== FECHAMENTO DO CAIXA =====")
print(f"Quantidade de vendas: {quantidadeVendas}")
print(f"Faturamento: R$ {faturamento:.2f}")
print(f"Ticket médio: R$ {ticketMedio:.2f}")
print(f"Maior venda: R$ {maiorVenda:.2f}")
print(f"Vendas em dinheiro: {qtdDinheiro}")
print(f"Vendas no Pix: {qtdPix}")
print(f"Vendas no cartão: {qtdCartao}")