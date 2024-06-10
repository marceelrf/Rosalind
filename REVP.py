from Bio import SeqIO

def reverse_complement(dna):
    """Returns the reverse complement of a DNA sequence."""
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complement[base] for base in reversed(dna))

# def ler_fasta(sequence):
#     record = SeqIO.parse(sequence, "fasta")
#     return record.seq

record = next(SeqIO.parse('Datasets/rosalind_revp (1).txt', "fasta"))

sequence = str(record.seq)
sequence
# seq1 = "ATGCAT"
# revc = reverse_complement(seq1)
# revc
# sequence = "TCAATGCATGCGGGTCTATATGCAT"

result = []
for bases in range(4,13):
    
    for i in range(0,len(sequence)-bases):
        
        seq1 = sequence[i:i+bases]
        
        revc = reverse_complement(seq1)
        print(f"{seq1} {revc}")
        if seq1 == revc:
            result.append(f"{i+1} {bases}")
            
            
result


for i in result:
    print(i)
    
# Specify the output file path
output_file = "Output/revp_output.txt"

# Open the file in write mode
with open(output_file, "w") as file:
    # Iterate over each string in the array
    for item in result:
        # Write each item to the file on a new line
        file.write(f"{item}\n")