# 1. Crie o dicionário com 3 contatos
# 2. Adicione um novo contato
# 3. Busque o telefone de uma pessoa
# 4. Remova um contato
# 5. Mostre todos os contatos em formato amigável

# 1. Crie o dicionário com 3 contatos -> ok
# lista de dicionários
contatos = [
    {'nome': 'João', 'número': 11987675423},
    {'nome': 'Mateus', 'número': 11990875324},
    {'nome': 'Victor', 'número': 11923456781}
]

print('AGENDA INICIAL:')
for pessoa in contatos:
    print(f" • {pessoa['nome']}: {pessoa['número']}")
print(f'Total Inicial: {len(contatos)} contatos')

print("\n" + "="*40)
# 2. Adicione um novo contato
print("ADICIONANDO PEDRO:")

novo_contato = {'nome':'Pedro', 'número': 11966778899,}
contatos.append(novo_contato)
print(contatos)

print('Pedro adionado!')
print("\n" + "="*40)

# 3. Busque o telefone de uma pessoa
print('BUSCANDO TELEFONE DO JOÃO:')

print(f"Telefone de João: {contatos[0]['número']}")

print("\n" + "="*40)

# 4. Remova um contato
# O método pop() em listas espera um ÍNDICE (número), não uma string
print('REMOVENDO JOÃO:')
pessoa_removida = contatos.pop(0)
print(f"Removido: {pessoa_removida['nome']} - Tel: {pessoa_removida['número']}")
print(f'Total restante: {len(contatos)} contatos')

print("\n" + "="*40)

# 5. Mostre todos os contatos em formato amigável
print('AGENDA TELEFÔNICA')
print('=' * 30)

for i, pessoa in enumerate(contatos,1):
    print(f"{i}. {pessoa['nome']}: {pessoa['número']}")
    
print('=' * 30)
print(f'Total: {len(contatos)} contatos')
