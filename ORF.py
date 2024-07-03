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



# seq = read_fasta('Datasets/rosalind_orf (3).txt')

seq = "AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG"
seq



# def transcribe(dna):
#     """Transcribes DNA to RNA by replacing all 'T's with 'U's."""
#     return dna.replace('T', 'U')

# def reverse_complement(dna):
#     """Returns the reverse complement of a DNA sequence."""
#     complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
#     return ''.join(complement[base] for base in reversed(dna))

# def translate(rna):
#     """Translates RNA sequence into a protein sequence."""
#     protein = []
#     for i in range(0, len(rna) - 2, 3):
#         codon = rna[i:i+3]
#         amino_acid = codon_dict.get(codon)
#         if amino_acid == 'Stop':
#             break
#         if amino_acid:
#             protein.append(amino_acid)
#     return ''.join(protein)


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



def translate_codon(codon):
    protein = None
    if len(codon) == 3 and codon in codon_dict:
        protein = codon_dict[codon]
    return protein


def reverse_complement(dna):
    lookup = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    return ''.join([lookup[c] for c in reversed(dna)])

def possible_protein_strings(s):
    results = []
    indices = []

    l = len(s)
    for i in range(l):
        protein = translate_codon(s[i:i+3])
        if protein and protein == 'M':
            indices.append(i)

    for i in indices:
        found_stop = False
        protein_string = ''

        for j in range(i, l, 3):
            protein = translate_codon(s[j:j+3])

            if not protein:
                break

            if protein == 'Stop':
                found_stop = True
                break

            protein_string += protein

        if found_stop:
            results.append(protein_string)

    return results

if __name__ == "__main__":

    small_dataset = "AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG"
    large_dataset = open('Datasets/rosalind_orf (5).txt').read().strip()

    possible_a = possible_protein_strings(large_dataset)
    possible_b = possible_protein_strings(reverse_complement(large_dataset))
    print("\n".join(set(possible_a + possible_b)))