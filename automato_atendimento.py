import random

# Definições do automato
alfabeto = ["Facil", "Moderado", "Dificil"]
alfabeto_pontos = {"Facil": 1, "Moderado": 2, "Dificil": 3}
estado_atual = {"Fila_1": 0, "Fila_2": 0, "Fila_3": 0}

# Atendimento Fácil: 1 ponto
# Atendimento Moderado: 2 pontos
# Atendimento Difícil: 3 pontos

# Estabelece condições de parada, visando o estado final
def filas_equivalentes():
    atendimentos = [estado_atual[fila] for fila in estado_atual]
    return len(set(atendimentos)) == 1 and all(pontuacao != 0 for pontuacao in atendimentos)

# Mostra o estado atual das filas
def output_estado():    
    for fila, pontos in estado_atual.items():
        print(f"{fila} está com {pontos} pontos")

# Mostra o estado inicial das filas
print("Estado inicial das filas: \n")
output_estado()

# Enquanto as condições não são satisfeitas, o laço é executado
while not filas_equivalentes():

    # Faz com que os tipos de atendimentos entrem de forma aleatória
    random.shuffle(alfabeto) 

    for tipo_atendimento in alfabeto:

        # Direciona o atendimento para a fila com menor pontuação
        fila_atual = min(estado_atual, key = estado_atual.get)
        estado_atual[fila_atual] += alfabeto_pontos[tipo_atendimento]        
        
        print(f"Atendimento '{tipo_atendimento}' direcionado para a fila:\n")
        output_estado()
        print("=====================================\n")

# Mostra o estado final das filas
print("Estado final das filas")
output_estado()

