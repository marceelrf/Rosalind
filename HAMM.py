import os

def hamming(s1, s2):
    dist = 0

    if len(s1) != len(s2):
        print("Sequências com tamanhos distintos")
        return None
    else:
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                dist += 1
    return dist

def ler_arquivo(filename):
    with open(filename, 'r') as file:
        linhas = file.readlines()
        if len(linhas) < 2:
            print("O arquivo não tem linhas suficientes")
            return None, None
        s1 = linhas[0].strip()
        s2 = linhas[1].strip()
        return s1, s2

# Exemplo de uso:
s1, s2 = ler_arquivo('Datasets/rosalind_hamm.txt')

#s1 = 'ATCG'
#s2 = 'AACG'

hamming(s1,s2)