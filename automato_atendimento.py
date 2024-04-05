# Função que representa um Autômato Finito Determinístico
def afd(M, w):
    
    # 'extrai' os elementos da tupla M
    δ, q, F = M
    
    # Dicionário para mapear os tipos de atendimento
    tipo_atendimento = {'1': 'Fácil', '2': 'Moderado', '3': 'Difícil'}
   
    # Itera sobre cada tipo de atendimento na sequência w
    for s in w:
        
        # Atualiza o estado atual
        q = δ[q, s]
    
        print(f"Novo atendimento - Tipo {s} {tipo_atendimento[s]}")
        print(f"Estado atual: {q}")
        print("Atendimento direcionado:")
        
        for transicao, estado in δ.items():
            if transicao == (q, s):
                print(f"  -> Transição: {transicao}")
                if estado == '000':
                    print(f"  -> Estado final: {estado}")
                else:
                    print(f"  -> Estado atualizado: {estado}")

        print("\n")
    
    return q in F

# Função de transição
δ = {
    ('000', '1'): '100',
    ('000', '2'): '200',
    ('000', '3'): '300',
    ('100', '1'): '110',
    ('100', '2'): '120',
    ('100', '3'): '130',
    ('200', '1'): '120',
    ('200', '2'): '220',
    ('200', '3'): '230',
    ('300', '1'): '130',
    ('300', '2'): '230',
    ('300', '3'): '330',
    ('110', '1'): '000',
    ('110', '2'): '112',
    ('110', '3'): '113',
    ('120', '1'): '112',
    ('120', '2'): '122',
    ('120', '3'): '123',
    ('130', '1'): '113',
    ('130', '2'): '123',
    ('130', '3'): '133',
    ('220', '1'): '122',
    ('220', '2'): '000',
    ('220', '3'): '223',
    ('230', '1'): '123',
    ('230', '2'): '223',
    ('230', '3'): '233',
    ('330', '1'): '133',
    ('330', '2'): '233',
    ('330', '3'): '000', 
    ('112', '1'): '110',
    ('112', '2'): '120',
    ('112', '3'): '130',
    ('113', '1'): '120',
    ('113', '2'): '220',
    ('113', '3'): '230',
    ('122', '1'): '000',
    ('122', '2'): '112', #223?
    ('122', '3'): '113', #?
    ('123', '1'): '112', #223?
    ('123', '2'): '122', #223?
    ('123', '3'): '123', #?
    ('133', '1'): '122', #233?
    ('133', '2'): '000',
    ('133', '3'): '223', #?    
    ('223', '1'): '110',
    ('223', '2'): '120',
    ('223', '3'): '130',
    ('233', '1'): '000',
    ('233', '2'): '112', #?
    ('233', '3'): '113'}

# Função de transição (δ), estado inicial (q) e conjunto de estados finais (F)
M = (δ, '000', ['000'])

# Teste da função
result = afd(M, '113211')

print(result)
