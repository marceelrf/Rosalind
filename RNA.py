import os

# Caminho para o arquivo
caminho_do_arquivo_read = 'Datasets/rosalind_rna.txt'
caminho_do_arquivo_save = 'Datasets/rosalind_rna_save.txt'
#os.path.abspath('Datasets/rosalind_dna.txt')
# Abrindo o arquivo e lendo a linha
with open(caminho_do_arquivo_read, 'r') as arquivo:
    DNA = arquivo.readline().strip()

RNA = DNA.replace("T","U")

# Abrindo o arquivo em modo de escrita e escrevendo a string
with open(caminho_do_arquivo_save, 'w') as arquivo:
    arquivo.write(RNA)


