# Dicionário: produto -> quantidade em estoque

# 1. Venda: reduza a quantidade de "camiseta" em 5
# 2. Reposição: aumente "calça" em 10
# 3. Novo produto: adicione "meias" com 100 unidades
# 4. Mostre apenas produtos com menos de 40 unidades
# 5. Calcule o total de itens no estoque

estoque = {"camiseta": 50, "calça": 30, "tenis": 25}

print('===== ESTOQUE INICIAL =====')
for i, (produto, quantidade) in enumerate(estoque.items(),1):
        print(f'{i} {produto}: {quantidade} unidades' )

print("=" * 40)

#1. Venda: reduza a quantidade de "camiseta" em 5
print('REDUZINDO A QUANTIDADE DE CAMISETAS EM "5" ')
estoque['camiseta'] = estoque['camiseta'] - 5
print(estoque)

print("=" * 40)

# 2. Reposição: aumente "calça" em 10
print('AUMENTANDO CALÇA EM "10" ')
estoque['calça'] = estoque['calça'] + 10
print(estoque)

print("=" * 40)

#3. Novo produto: adicione "meias" com 100 unidades
print('ADICIONANDO O PRODUTO "MEIAS"')
estoque['meias'] = 100
print(estoque)

print("=" * 40)

# 4. Mostre apenas produtos com menos de 40 unidades
print('PRODUTOS MENORES QUE "40 UNIDADES"')
for produto, quantidade in estoque.items():
    if quantidade < 40:
        print(f'• {produto}: {quantidade}')

print("=" * 40)

# 5. Calcule o total de itens no estoque
print(f'Total de Itens: {len(estoque)} Itens')

print("=" * 40)

print('===== ESTOQUE ATUAL =====')
for i, (produto, quantidade) in enumerate(estoque.items(),1):
        print(f'{i} {produto}: {quantidade} unidades' )