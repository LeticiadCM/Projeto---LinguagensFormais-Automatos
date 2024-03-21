#Definições do automato
estados = ["Cheia", "Moderada", "Vazia"]
alfabeto = ["Rapido", "Normal", "Demorado"]
alfabeto_pontos = {"Rapido": 1, "Normal": 2, "Demorado": 5}
estado_atual = {"Fila_1": 0, "Fila_2": 0, "Fila_3": 0}

#Rápido: 1 ponto
#Normal: 2 pontos
#Demorado: 5 pontos

#função que vai sempre escolher a fila com menor pontuação
def escolher_fila():

    fila_menor_pont = min(estado_atual, key = estado_atual.get)
    return fila_menor_pont

#atualiza o estado conforme a pontuação
def atualizar_estado(fila):

    pontos_estado = estado_atual[fila]

    if pontos_estado <= 0:
        return "Vazia"
    elif 1 <= pontos_estado <= 5:
        return "Moderada"
    elif pontos_estado >= 6: 
        return "Cheia"

def output_estado():

    for fila, pontos_estado in estado_atual.items():

        estado = atualizar_estado(fila)
        print(f"{fila} está {estado}")

#Mostra o estado incial em que as filas estão vazias
print("Estado inicial das filas: \n")
output_estado()

for tipo_atendimento in alfabeto:

    if tipo_atendimento not in alfabeto:
        print("Tipo de atendimento inválido")
        continue

    #escolhe a melhor fila do atendimento atual
    fila_atual = escolher_fila()

    #adiciona pontos do alfabeto à fila escolhido
    estado_atual[fila_atual] += alfabeto_pontos[tipo_atendimento]

    print("\n Atualização das filas de atendimento: \n")
    output_estado()
    print("===================================== \n")

print("Estado atual após a atualização das filas:")
print(estado_atual)


