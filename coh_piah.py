import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
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
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
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
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    pass

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''

    lista_palavras = separa_palavras(texto)
    lista_sentencas = separa_sentencas(texto)
    lista_frases = separa_frases(texto)

    palavras_total = len(lista_palavras)
    sentencas_total = len(lista_sentencas)
    frases_total = len(lista_frases)

    palavras_tamanhos : int = 0
    palavras_diferentes = n_palavras_diferentes(lista_palavras)
    palavras_unicas = n_palavras_unicas(lista_palavras)

    caracteres_total : int = 0
    caracteres_frase : int = 0
    caracteres_pontuacao = [".", ",", "!", "?", ":", ";"]

    for palavra in lista_palavras:
        palavras_tamanhos += len(palavra)

        possui_pontuacao = False
        for pontuacao in caracteres_pontuacao:
            if pontuacao in palavra:
                caracteres_total += len(palavra) - 1
                possui_pontuacao = True
                
        if possui_pontuacao: continue

        caracteres_total += len(palavra)

    wal = palavras_tamanhos / palavras_total
    print("Tamanho médio de palavra: " + str(wal))

    ttr = palavras_diferentes / palavras_total
    print("Relação Type-Token: " + str(ttr))

    hlr = palavras_unicas / palavras_total
    print("Relação Hapax Legomana: " + str(hlr))

    sal = caracteres_total / sentencas_total
    print("Tamanho médio da sentença: " + str(sal))

    sac = frases_total / sentencas_total
    print("Complexidade de sentença: " + str(sac))

    pal = palavras_total / frases_total
    print("Tamanho médio de frase: " + str(pal))

    return [wal, ttr, hlr, sal, sac, pal]

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    pass

calcula_assinatura("Eu amo o bolo que o Chico faz.")