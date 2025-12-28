# CALCULADORA SIMPLES:

def calculadora():
    
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite outro número: '))
    
    op = input('Escolha a operação (+, -, x, /): ')
    
    if op == '+':
        resultado = n1 + n2
        print(f'O resultado de {n1} + {n2} = {resultado}')
        
    elif op == '-':
        resultado = n1 - n2
        print(f'O resultado de {n1} - {n2} = {resultado}')
        
    elif op == '*' or op == 'x':
        resultado = n1 * n2
        print(f'O resultado de {n1} * {n2} = {resultado}')
        
    elif op == '/':
        if n2 == 0:
            print("Erro: divisão por zero!")
        else:
            resultado = n1 / n2
            print(f'O resultado de {n1} - {n2} = {resultado:.2f}')
            
    else:
        print("Operação inválida! Use +, -, x, ou /")
            
            
calculadora()
