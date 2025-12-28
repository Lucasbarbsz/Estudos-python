# ORGANIZADOR DE DESPESAS PESSOAIS

# Adicionar despesa (data, valor, categoria, descrição)

# Ver resumo mensal (total gasto, por categoria)

# Definir orçamento por categoria

# Alertas se passar do orçamento

# Exportar para Excel/CSV

from datetime import datetime

def pedir_despesas():

# validação de data:

     while True:
          data_str = input('Data (DD/MM/AAAA):')
          try:
               data = datetime.strptime(data_str, "%d/%m/%Y")
               break
          except ValueError:
               print('Data inválida, use: "(DD/MM/AAAA)"')


# validação de valor:
     while True:
          valor_str = input('Valor R$: ').replace(',','.')
          try:
               valor = float(valor_str)
               if valor < 0:
                    print('Valor deve ser positivo')
               else:
                    break
          except ValueError:
               print('Valor inválido, digite um número.')


# Menu CATEGORIAS:
     categorias = ['Alimentação', 'Moradia', 'Investiementos', 'Outros']
     print('\nCategorias disponíveis:')

     for i, cat in enumerate(categorias,1):
          print(f'{i}. {cat}')

     while True:
        try:
            escolha = int(input(f"Escolha (1-{len(categorias)}): "))
            if 1 <= escolha <= len(categorias):
                categoria = categorias[escolha-1]
                break
            else:
                print(f"Escolha entre 1 e {len(categorias)}")
        except ValueError:
            print("Digite um número!")
    
     descricao = input("Descrição: ").strip()
    
     return {
        "data": data.strftime("%d/%m/%Y"),
        "valor": valor,
        "categoria": categoria,
        "descricao": descricao
    }

pedir_despesas()

