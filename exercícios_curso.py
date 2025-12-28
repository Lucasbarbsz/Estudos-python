# função format:
# ele agrega os valores na sequência do format -> format(a,b,c,d)
# pode usar os índices para não depender da ordem de colocação do código: 'meu nome é {1},
# e sou casado com a {4}.
a = 'Lucas'
b = 'Luffy'
c = 'Mines'
d = 'Luana'

formato = 'eu sou o {}, tenho dois gatinhos, que são o {} e a {} e sou casado com a {}'.format(a,b,c,d)
print(formato)


#if, else, elif:

entrada = input('Você quer "entrar" ou "sair: \n')

if entrada.lower() == "entrar":
    print('Pode entrar')
elif entrada.lower() == "sair":
    print('Pode sair')
else:
    print('Error: Digite uma opção válida!')

# For 

letra = 'python'

for i in letra:
    print(i)

#verificar se o elemento é iterável:

def e_iteravel(obj):
    try:
        for _ in obj:
            return True
    except TypeError:
        return False
    
print(e_iteravel([1,2,3]))
print(e_iteravel([22]))



         
