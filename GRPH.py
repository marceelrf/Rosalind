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

seq = import_multi_fasta("Datasets/test_GRPH.txt")

str(seq[0].seq)