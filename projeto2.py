# LISTA DE TAREFAS INTELIGENTE

# Adicionar tarefa (nome, prioridade: 1-5, data limite)

# Listar tarefas ordenadas por prioridade/data

# Marcar como concluída

# Buscar tarefas por palavra-chave

# Lembretes de tarefas próximas do prazo

class Tarefa:
    def __init__(self, nome, prioridade, data_limite):
        self.nome = nome
        self.prioridade = prioridade
        self.data_limite = data_limite
        self.concluida = False


    def __str__(self):
        status = '✓' if self.concluida else ''
        return f'[{status}] {self.nome} (Prioridade: {self.prioridade}, Data: {self.data_limite})'
    
tarefas = [
    Tarefa("Estudar Python", 1, "2024-01-20"),
    Tarefa("Fazer compras", 3, "2024-01-18")
]

print('======== SUAS TAREFAS ==========')
for i, tarefa in enumerate(tarefas, 1):
    print(f'{i}. {tarefa}')




    
        