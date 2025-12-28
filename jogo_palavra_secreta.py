palavra_secreta = 'churrasco'

lista = []
tentativas = 0

while True:
    letra_digitada = input('Digite uma letra: ').lower()
    tentativas += 1
    if tentativas > 10:
        print('Acabou suas tentativas')
        print(f'A palavra secreta era: {palavra_secreta}')
        break  

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra')
        continue

    if letra_digitada in palavra_secreta:
        lista += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in lista:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print('palavra_formada:', palavra_formada)

    if palavra_formada == palavra_secreta:
        print('PARABÉNS, VOCÊ ACERTOU A PALAVRA!')
        print('Tentaivas:', tentativas)
        print('Letras tentadas:', lista)
        break
        