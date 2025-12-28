# 🔤 Exercício 3: Verificador de Palíndromo
# Escreva uma função que:

# Recebe uma string 

# Verifica se é um palíndromo (lê-se igual de trás pra frente)

# Ignora maiúsculas/minúsculas e espaços 

# Retorna True ou False 


palavra = input('Digite uma palavra: ')

texto = palavra.lower()
texto = texto.replace(" ", "")

texto_invertido = "".join(reversed(texto))

if texto == texto_invertido:
    print('É palíndromo')

else:
    print('Não é palíndromo')



#replace -> substitue um elemento por outro:
# EXEMPLO:
primeiro_gato = 'tom'

substituicao_nome = primeiro_gato.replace('tom','luffy')
print(substituicao_nome)





