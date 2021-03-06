'''
ATIVIDADE FINAL

GUSTAVO HENRIQUE S. RIBEIRO - https://github.com/gustavohsr

'''
import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")

    wal = float(input("Entre o tamanho medio de palavra:"))
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

def compara_assinatura(as_a,as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de 
    similaridade nas assinaturas.'''
    soma = 0
    for index in range(0,6):
        soma = soma + (abs(as_a[index] - as_b[index]))

    return soma / 6

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    wal = float(tam_medio_palavra(texto))
    ttr = float(type_token(texto))
    hlr = float(hapax_legomana(texto))
    sal = float(tam_medio_sentenca(texto))
    sac = float(complexidade(texto))
    pal = float(tam_medio_frase(texto))

    return [wal, ttr, hlr, sal, sac, pal]

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e 
    deve devolver o numero (1 a n) do texto com maior probabilidade de ter
    sido infectado por COH-PIAH.'''
    menor_grau_similaridade = compara_assinatura(ass_cp,calcula_assinatura(textos[1]))
    text_index = 0
    for index in range(len(textos)):
        calc_ass = calcula_assinatura(textos[index])
        grau_similaridade = compara_assinatura(ass_cp,calc_ass)
        if grau_similaridade < menor_grau_similaridade:
            text_index = index
    return index

def conta_caracteres(texto):
    '''A funcao recebe uma texto e devolve a quantidade de caracteres'''
    return len(texto)

def tam_medio_palavra(texto):
    '''Tamanho médio de palavra é a soma dos tamanhos das 
    palavras dividida pelo número total de palavras.'''

    num_carac = len(texto_puro(texto))
    num_palavras = len(separa_palavras(texto))

    return float(num_carac / num_palavras)

def type_token(texto):
    '''Relação Type-Token é o número de palavras diferentes dividido pelo número total de palavras.'''
    num_palavras_diff = n_palavras_diferentes(separa_palavras(texto))

    return float(num_palavras_diff / len(separa_palavras(texto)))

def hapax_legomana(texto):
    '''Razão Hapax Legomana: Número de palavras utilizadas uma vez dividido pelo número total de palavras.'''
    num_palavras_unicas = n_palavras_unicas(texto)
    
    return float(num_palavras_unicas / len(separa_palavras(texto)))

def tam_medio_sentenca(texto):
    '''Tamanho médio de sentença é a soma dos números de caracteres em todas as sentenças 
    dividida pelo número de sentenças (os caracteres que separam uma sentença da outra 
    não devem ser contabilizados como parte da sentença).'''
    
    num_caracteres = len(texto_puro(texto))
    num_sentencas = len(separa_sentencas(texto))

    return float(num_caracteres / num_sentencas)

def texto_puro(texto):
    '''Retira todos os caracteres que separam sentenças e frases'''
    a = separa_sentencas(texto)
    listToStr = ' '.join(map(str, a)) 
    b = separa_frases(listToStr)
    listToStr = ' '.join(map(str, b)) 
    return listToStr

def complexidade(texto):
    '''Complexidade de sentença é o número total de frases divido pelo número de sentenças.'''
    num_frases = len(separa_frases(texto))
    num_sentencas = len(separa_sentencas(texto))
    return float(num_frases / num_sentencas)

def tam_medio_frase(texto):
    '''Tamanho médio de frase é a soma do número de caracteres em cada frase dividida 
    pelo número de frases no texto (os caracteres que separam uma frase da outra não
    devem ser contabilizados como parte da frase).'''
    num_caracteres = len(texto_puro(texto))
    num_frases = len(separa_frases(texto))

    return float(num_caracteres / num_frases)

#========================================###===================
ass_cp = le_assinatura()
texts = le_textos()

result = avalia_textos(texts,ass_cp)

print("O autor do texto ", result," está infectado com COH-PIAH")
#===============================================================