import sys
sys.path.append('/py_funs/')

from Bio import SeqIO

def import_multi_fasta(file_path):
    """
    Import sequences from a multi-FASTA file.

    Parameters:
    file_path (str): The path to the multi-FASTA file.

    Returns:
    list: A list of SeqRecord objects.
    """
    sequences = []
    try:
        for record in SeqIO.parse(file_path, "fasta"):
            sequences.append(record)
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
    return (sequences)

seq = import_multi_fasta("/home/marceelrf/Projs/Rosalind/Datasets/rosalind_grph.txt")
seq
# str(seq[0].seq)[-3:]
# str(seq[0].seq)[0:3]

res = []
for i in range(len(seq)):
    print(i)
    
    s1 = seq[i]
    
    for j in range(len(seq)):
        if i != j:
            
            s2 = seq[j]
            if str(s1.seq)[-3:] == str(s2.seq)[0:3]:
                
                res.append(f"{s1.id} {s2.id}")
                
res

with open("Output/GRPH.txt", 'w') as arquivo:
    for line in res:

        arquivo.write(f"{line}\n")