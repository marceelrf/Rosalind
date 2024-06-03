import os 

complement = {
    'A': 'T',
    'T': 'A',
    'C': 'G',
    'G': 'C'
}


# Caminho para o arquivo
caminho_do_arquivo_read = 'Datasets/rosalind_revc.txt'
caminho_do_arquivo_save = 'Datasets/rosalind_revc_save.txt'

with open(caminho_do_arquivo_read, 'r') as arquivo:
    DNA = arquivo.readline().strip()

reverse_complement = "".join(complement.get(base, base) for base in reversed(DNA))

# Abrindo o arquivo em modo de escrita e escrevendo a string
with open(caminho_do_arquivo_save, 'w') as arquivo:
    arquivo.write(reverse_complement)

print(reverse_complement)