# 🧠 DESAFIO 6 — Intermediário (importante 🔥)

# Crie um programa que:

# Comece com:

# frutas = {}


# Peça ao usuário:

# nome da fruta

# quantidade

# Adicione ao dicionário

# Se a fruta já existir:

# some a quantidade ao valor atual

# 📌 Exemplo:

# Entrada: maçã, 3
# Entrada: maçã, 2
# Resultado: {'maçã': 5}

frutas = {}

while True:
    nome_fruta = input('Me diga o nome da fruta (ou "sair" para encerrar): ').lower()

    if nome_fruta == "sair":
        break

    quantidade_fruta = int(input('Me diga a quantidade: '))

    if nome_fruta in frutas:
        frutas[nome_fruta] += quantidade_fruta
    else:
        frutas[nome_fruta] = quantidade_fruta

    print('\nFrutas cadastradas:')
    for fruta,quantidade in frutas.items():
        print(f'{frutas}')