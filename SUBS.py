import os


#Importar o arquivo.
#primeira linha ser a sequencia
#segunda linha o motif

def ler_arquivo(filename):
    with open(filename, 'r') as file:
        linhas = file.readlines()
        if len(linhas) < 2:
            print("O arquivo não tem linhas suficientes")
            return None, None
        DNA = linhas[0].strip()
        motif = linhas[1].strip()
        return DNA, motif
    

DNA, motif = ler_arquivo('Datasets/rosalind_subs.txt')

kmer = len(motif)

pos_dict = []

for i in range(len(DNA)-kmer-1):
    s1 = DNA[i:(i+kmer)]

    if s1 == motif:
        pos_dict.append(i+1)

print(pos_dict)
