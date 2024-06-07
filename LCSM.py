from Bio import SeqIO

#Funcoes -------------------------------------

def import_fasta_sequences(fasta_file):
    """
    Importa todas as sequências de um arquivo FASTA e as salva em uma lista.

    Parâmetros:
    fasta_file (str): O caminho para o arquivo FASTA.

    Retorna:
    list: Uma lista contendo todas as sequências do arquivo FASTA.
    """
    sequences = []
    for record in SeqIO.parse(fasta_file, "fasta"):
        sequences.append(str(record.seq))
    return sequences

def generate_kmers(sequence, k):
    """
    Gera todos os k-mers de uma sequência de DNA ou RNA.

    Parâmetros:
    sequence (str): A sequência de DNA ou RNA.
    k (int): O comprimento dos k-mers.

    Retorna:
    list: Uma lista contendo todos os k-mers da sequência.
    """
    kmers = [sequence[i:i+k] for i in range(len(sequence) - k + 1)]
    return kmers

def find_shortest_sequence_length(sequences):
    """
    Calcula o comprimento da menor sequência em uma lista de sequências.

    Parâmetros:
    sequences (list): Uma lista contendo sequências de DNA ou RNA.

    Retorna:
    int: O comprimento da menor sequência.
    """
    if not sequences:
        return 0  # Retorna 0 se a lista estiver vazia

    # Calcula o comprimento de cada sequência e retorna o menor
    min_length = min(len(seq) for seq in sequences)
    return min_length

def find_shortest_sequence_in_array(sequences):
    """
    Retorna a sequência de menor tamanho em um array de sequências de DNA.

    Parâmetros:
    sequences (list): Uma lista de strings representando sequências de DNA.

    Retorna:
    str: A sequência de menor tamanho.
    """
    if not sequences:
        return None  # Retorna None se o array estiver vazio

    shortest_sequence = min(sequences, key=len)
    return shortest_sequence

def contains_motif(sequence, motif):
    """
    Verifica se uma sequência de DNA contém um determinado motif.

    Parâmetros:
    sequence (str): A sequência de DNA.
    motif (str): O motif a ser procurado na sequência.

    Retorna:
    bool: True se a sequência contém o motif, False caso contrário.
    """
    return motif in sequence

#Teste
#generate_kmers("AGCTAGCTAG",3)
kmer_tmp = generate_kmers("AGCTAGCTAG",len("AGCTAGCTAG")-2)
contains_motif("AGCTAGCTAG",kmer_tmp[0])


obj = import_fasta_sequences("Datasets/test_LCSM.txt")
obj

find_shortest_sequence_length(obj)
find_shortest_sequence_in_array(obj)
contains_motif(obj[1],"AG")


# Analise

def LCSM(fasta_file):
    sequences = import_fasta_sequences(fasta_file)

    min_seq = find_shortest_sequence_in_array(sequences)

    #Motif_equal = False

    it = len(min_seq)

    motifs_present = []
    while it > 1:

        kmers = generate_kmers(min_seq,it)

        for i in kmers:
            
            if kmers[i] == True:
                motifs_present.append(kmers[i])

        it = it - 1 

    return motifs_present

def LCSM(fasta_file):
    sequences = import_fasta_sequences(fasta_file)
    min_seq = min(sequences, key=len)  # Find the shortest sequence directly

    motifs_present = []

    for length in range(len(min_seq), 1, -1):  # Start from the longest possible substring
        kmers = generate_kmers(min_seq, length)
        
        for kmer in kmers:
            if all(kmer in seq for seq in sequences):  # Check if kmer is in all sequences
                motifs_present.append(kmer)

        if motifs_present:
            break  # Stop once the longest common motifs are found

    return motifs_present


LCSM('Datasets/rosalind_lcsm.txt')