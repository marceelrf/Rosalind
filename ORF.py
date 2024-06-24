from Bio import SeqIO


#Funções ---------------------------------------------
def read_fasta(filename):
    """Reads a FASTA file and returns a list of DNA sequences."""
    sequences = []
    with open(filename, 'r') as file:
        sequence = ''
        for line in file:
            if line.startswith('>'):
                if sequence:
                    sequences.append(sequence)
                    sequence = ''
            else:
                sequence += line.strip()
        if sequence:
            sequences.append(sequence)
    return sequences

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


# seq = read_fasta('Datasets/rosalind_orf (3).txt')

seq = "AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG"
seq



def transcribe(dna):
    """Transcribes DNA to RNA by replacing all 'T's with 'U's."""
    return dna.replace('T', 'U')

def reverse_complement(dna):
    """Returns the reverse complement of a DNA sequence."""
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complement[base] for base in reversed(dna))

def translate(rna):
    """Translates RNA sequence into a protein sequence."""
    protein = []
    for i in range(0, len(rna) - 2, 3):
        codon = rna[i:i+3]
        amino_acid = codon_dict.get(codon)
        if amino_acid == 'Stop':
            break
        if amino_acid:
            protein.append(amino_acid)
    return ''.join(protein)


def find_orfs(dna):
    """Finds all distinct ORFs in the given DNA sequence and its reverse complement."""
    orfs = set()
    sequences = [dna, reverse_complement(dna)]
    for seq in sequences:
        rna = transcribe(seq)
        for frame in range(3):
            for i in range(frame, len(rna) - 2, 3):
                if rna[i:i+3] == 'AUG':
                    protein = translate(rna[i:])
                    if protein:
                        orfs.add(protein)
    return orfs

def find_motif_positions(sequence, motif):
    positions = []
    motif_length = len(motif)
    for i in range(len(sequence) - motif_length + 1):
        if sequence[i:i + motif_length] == motif:
            positions.append(i)
    return positions

print(codon_dict.get("AGC"))
print(codon_dict.items())
# seq[0]
# ORFs = find_orfs(seq[0])

# for seq in ORFs:
#     print(f"{seq}")
codon_dict.setdefault("AUG")

while i < len(seq):
    
    if seq[i:i+3] == "AUG":
        