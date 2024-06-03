from Bio import SeqIO

def ler_fasta(arquivo_fasta, funcao):
    maior_porcentagem = 0
    melhor_sequencia = None
    melhor_id = None

    with open(arquivo_fasta, "r") as arquivo:
        for record in SeqIO.parse(arquivo, "fasta"):
            resultado = funcao(record.seq)
            if resultado > maior_porcentagem:
                maior_porcentagem = resultado
                melhor_sequencia = record.seq
                melhor_id = record.id

    return melhor_id, melhor_sequencia, maior_porcentagem

def calcular_porcentagem_CG(sequencia):
    contador_CG = sequencia.count('C') + sequencia.count('G')
    porcentagem_CG = (contador_CG / len(sequencia)) * 100
    return porcentagem_CG

# Substitua 'seu_arquivo.fasta' pelo caminho para o seu arquivo FASTA
melhor_id, melhor_sequencia, maior_porcentagem = ler_fasta('Datasets/rosalind_gc.txt', calcular_porcentagem_CG)

print(f"Identificador com maior porcentagem CG: {melhor_id}")
print(f"Sequência: {melhor_sequencia}")
print(f"Porcentagem CG: {maior_porcentagem:.2f}%")

print(f"{melhor_id}\n{maior_porcentagem}")


