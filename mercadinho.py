import random

#Lista com uma sequencia de dicionarios para armazenar os produtos, com seu preço e quantidade
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

for produto in produtos:
    print(f'{produto["nome"]} {produto["preco"]:.2f} {produto["quantidade"]}')
    print()