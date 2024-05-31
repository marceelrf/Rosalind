import os

# Caminho para o arquivo
caminho_do_arquivo = 'Datasets/rosalind_dna.txt'
#os.path.abspath('Datasets/rosalind_dna.txt')
# Abrindo o arquivo e lendo a linha
with open(caminho_do_arquivo, 'r') as arquivo:
    DNA = arquivo.readline().strip()

# Exibindo o conteúdo da linha
print(DNA)

A_count = DNA.count("A")
C_count = DNA.count("C")
G_count = DNA.count("G")
T_count = DNA.count("T")

print(f"{A_count} {C_count} {G_count} {T_count}")
