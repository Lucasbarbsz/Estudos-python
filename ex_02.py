# 📊 Exercício 2: Analisador de Números
# Faça um programa que:

# Recebe 5 números do usuário

# Identifica o maior e o menor

# Calcula a média

# Conta quantos são pares e ímpares

def analisador():
    
    numeros = []
    
    print("Vou analisar 5 números para você!")
    
    for i in range(5):
        num = float(input(f"Digite o {i+1}º número: "))
        numeros.append(num)
        
    maior = max(numeros)
    menor = min(numeros)
    
    media = sum(numeros) / len(numeros)
    
    pares = 0
    impares = 0
    for num in numeros:
        if num % 2 == 0:
            pares += 1
        else:
            impares += 1
            
    print(f"\n=== RESULTADOS ===")
    print(f"Números: {numeros}")
    print(f"Maior: {maior}")
    print(f"Menor: {menor}")
    print(f"Média: {media:.2f}")
    print(f"Pares: {pares}")
    print(f"Ímpares: {impares}")
    
analisador()


   



    






