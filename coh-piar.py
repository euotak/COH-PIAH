import re

def le_assinatura():

    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():

    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):

    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):

    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    return frase.split()

def n_palavras_unicas(lista_palavras):

    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):

    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    grau = sum(abs(as_a[i] - as_b[i]) for i in range(6)) / 6
    return grau

def calcula_assinatura(texto):    
    sentencas = separa_sentencas(texto)
    num_sentencas = 0
    soma_car_sentencas = 0

    frases = []
    for i in range(len(sentencas)):
        frase_aux = separa_frases(sentencas[i])
        frases.append(frase_aux)
        num_sentencas += 1
        soma_car_sentencas = soma_car_sentencas + len(sentencas[i])

    palavras = []
    num_frases = 0
    soma_car_frases = 0
    for linha in range(len(frases)):
        for coluna in range(len(frases[linha])):
            palavras_aux = separa_palavras(frases[linha][coluna])
            palavras.append(palavras_aux)
            num_frases += 1
            soma_car_frases += len(frases[linha][coluna])

    mtrx_para_lista = []
    #COLOCA O QUE ESTÁ NA EM MATRIZ PARA UMA LISTA
    for linha in range(len(palavras)):
        for coluna in range(len(palavras[linha])):
            mtrx_para_lista.append(palavras[linha][coluna])
    palavras = mtrx_para_lista[:]
    total_letras = 0
    num_tot_palavras = len(palavras)
    #CALCULA A QUANTIDADE DE LETRAS
    for lin in range(len(palavras)):
        for col in range(len(palavras[lin])):
            total_letras = total_letras + len(str(palavras[lin][col]))
    
    tamMedPalavra = total_letras / num_tot_palavras
    typeToken = n_palavras_diferentes(palavras) / num_tot_palavras
    hapaxLegomana = n_palavras_unicas(palavras) / num_tot_palavras
    tamMedSentenca = soma_car_sentencas / num_sentencas
    comMedSentenca = num_frases / num_sentencas
    tamMedFrase = soma_car_frases / num_frases

    return [tamMedPalavra, typeToken, hapaxLegomana, tamMedSentenca, comMedSentenca, tamMedFrase]


def avalia_textos(textos, ass_cp):
    menor_grau = float('inf')
    texto_infectado = -1
    
    for i, texto in enumerate(textos):
        grau_similaridade = compara_assinatura(calcula_assinatura(texto), ass_cp)
        
        if grau_similaridade < menor_grau:
            menor_grau = grau_similaridade
            texto_infectado = i
    
    print("O autor do texto %d está infectado com COH-PIAH" % (texto_infectado + 1))
    return texto_infectado + 1



def main():
    assinatura_cp = le_assinatura()
    textos_lidos = le_textos()
    avalia_textos(textos_lidos, assinatura_cp) 

main()