from Bio import SeqIO

codon_dict = {
    'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
    'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
    'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',
    'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
    'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
    'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
    'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
    'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
    'UAU': 'Y', 'UAC': 'Y', 'UAA': 'Stop', 'UAG': 'Stop',
    'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
    'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
    'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
    'UGU': 'C', 'UGC': 'C', 'UGA': 'Stop', 'UGG': 'W',
    'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
    'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
    'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
}

def translate_mrna_to_protein(mRNA):
    # Dividir a sequência de mRNA em códons de 3 nucleotídeos
    codons = [mRNA[i:i+3] for i in range(0, len(mRNA), 3)]
    
    # Traduzir cada códon para o aminoácido correspondente
    protein_sequence = []
    for codon in codons:
        amino_acid = codon_dict.get(codon, 'Stop')  # Use 'Stop' como padrão se o códon não for encontrado
        if amino_acid == 'Stop':
            break
        protein_sequence.append(amino_acid)
    
    return ''.join(protein_sequence)

records = list(SeqIO.parse("Datasets/rosalind_splc (1).txt", "fasta"))

DNA = str(records[0].seq)
DNA
# DNA = DNA.replace(str(records[1].seq),"")

# DNA = DNA.replace(str(records[2].seq),"")

# RNA = DNA.replace("T","U")
# RNA 


for i in range(1,len(records)):
    print(i)
    DNA = DNA.replace(str(records[i].seq),"")
    
RNA = DNA.replace("T","U")
translate_mrna_to_protein(RNA)