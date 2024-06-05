import os
import math
import scipy

math.comb(4,2)

#Funções ---------------------------------------------
def ler_arquivo(filename):
    with open(filename, 'r') as file:
        linhas = file.readlines()
        vals = linhas[0].strip()
        return vals

# Função para converter string em três valores numéricos distintos
def string_para_numeros(string_valores):
    # Dividindo a string em uma lista de substrings
    lista_valores = string_valores.split()
    
    # Verificando se a lista contém exatamente três elementos
    if len(lista_valores) != 3:
        raise ValueError("A string deve conter exatamente três valores numéricos separados por espaço.")
    
    # Convertendo as substrings para inteiros
    k = int(lista_valores[0])
    m = int(lista_valores[1])
    n = int(lista_valores[2])
    
    return k, m, n


#Analise
vals = ler_arquivo('Datasets/rosalind_iprb (2).txt')


k, m, n = string_para_numeros(vals)
k, m, n = 2, 2, 2

pop = 4 * math.comb(k + m + n, 2)
pop
#total = k+m+n

#Probabilidades dos casais serem:

# dominant organisms         
dom_total = 4*math.comb(k,2) + 4*k*m + 4*k*n + 3*math.comb(m,2) + 2*m*n
dom_total
# probability for dominant organisms
phom = dom_total/pop
phom

Prob = Phet_res*(1/2) + Phet_het*(3/4) + 2*Pdom
Prob
#Resultados  = 0.78333