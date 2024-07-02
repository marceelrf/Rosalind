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


# def find_orfs(dna):
#     """Finds all distinct ORFs in the given DNA sequence and its reverse complement."""
#     orfs = set()
#     sequences = [dna, reverse_complement(dna)]
#     for seq in sequences:
#         rna = transcribe(seq)
#         for frame in range(3):
#             for i in range(frame, len(rna) - 2, 3):
#                 if rna[i:i+3] == 'AUG':
#                     protein = translate(rna[i:])
#                     if protein:
#                         orfs.add(protein)
#     return orfs


def find_orfs(dna, codon_dict):
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
    
    def get_frames(dna):
        """Generates all six reading frames of the given DNA sequence."""
        frames = []
        # Forward frames
        for i in range(3):
            frames.append(dna[i:])
        # Reverse frames
        rev_comp = reverse_complement(dna)
        for i in range(3):
            frames.append(rev_comp[i:])
        return frames
    
    def find_orfs_in_frame(frame):
        """Finds ORFs in a single frame."""
        orfs = []
        rna = transcribe(frame)
        protein = translate(rna)
        start_index = 0
        
        while start_index < len(protein):
            start_index = protein.find('M', start_index)
            if start_index == -1:
                break
            end_index = protein.find('*', start_index)
            if end_index == -1:
                break
            orfs.append(protein[start_index:end_index])
            start_index = end_index + 1
        
        return orfs
    
    frames = get_frames(dna)
    all_orfs = []
    
    for frame in frames:
        all_orfs.extend(find_orfs_in_frame(frame))
    
    return all_orfs

find_orfs(seq, codon_dict)