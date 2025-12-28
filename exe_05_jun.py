# 📊 DESAFIO 5: Encontrar o Elemento Único
# Problema: Dada uma lista onde todos os elementos aparecem DUAS vezes, exceto UM elemento que aparece apenas UMA vez, encontre esse elemento único.

# Restrições:

# Não usar contadores ou dicionários de forma óbvia

# Tentar solução com complexidade O(n) tempo e O(1) espaço

# A lista pode ter até 1 milhão de elementos
# Exemplos:
# [4, 1, 2, 1, 2] → 4
# [7, 3, 5, 3, 7] → 5
# Dica: Pense em operações bit a bit.

lista = [ 2,1,2,1,3]

def elemento_unico(lista):
    resultado = 0
    for num in lista:
        resultado = resultado ^ num
    return resultado
    
print(elemento_unico([2,1,2,1,3]))


