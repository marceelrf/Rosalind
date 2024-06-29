import re
import os
import requests
#from Bio import SeqIO

#Exemple
link = "https://rest.uniprot.org/uniprotkb/B5ZC00.fasta"

# import sequence
fasta = requests.get(link).text
print(fasta)

lines = fasta.split('\n')
sequence = ''.join(line.strip() for line in lines if not line.startswith('>'))

# find the motif
motif = re.compile(r'N[^P][ST][^P]')

# Find all matches in the protein sequence
matches = motif.finditer(sequence)

# Print the matches and their positions
for match in matches:
    start_pos = match.start()
    end_pos = match.end()
    matched_seq = match.group()
    print(f"Match: {matched_seq} at position {start_pos+1}-{end_pos+1}")
    
