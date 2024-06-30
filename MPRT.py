import re
import requests
#from Bio import SeqIO

# #Exemple
# link = "https://rest.uniprot.org/uniprotkb/B5ZC00.fasta"

# # import sequence
# fasta = requests.get(link).text
# print(fasta)

# lines = fasta.split('\n')
# sequence = ''.join(line.strip() for line in lines if not line.startswith('>'))

# # find the motif
# motif = re.compile(r'N[^P][ST][^P]')

# # Find all matches in the protein sequence
# matches = motif.finditer(sequence)

# # Print the matches and their positions
# for match in matches:
#     start_pos = match.start()
#     end_pos = match.end()
#     matched_seq = match.group()
#     print(f"Match: {matched_seq} at position {start_pos+1}-{end_pos+1}")




# Read the file content
with open("Datasets/rosalind_mprt (2).txt", "r") as file:
    content = file.read()

# Split the content into lines
UNIPROT_ACC = content.splitlines()

# Open the output file for writing
with open("output.txt", "w") as output_file:
    for code in UNIPROT_ACC:
        print("<----------------------------------->")
        print(code)
        print("\n")
        
        # Get the first part of the code
        code1 = code.split("_")[0]
        
        # Construct the URL
        link = f"https://rest.uniprot.org/uniprotkb/{code1}.fasta"
        
        # Fetch the sequence data
        response = requests.get(link)
        
        # Check if the request was successful
        if response.status_code == 200:
            fasta = response.text

            # Split the fasta into lines and join the sequence lines
            lines = fasta.split('\n')
            sequence = ''.join(line.strip() for line in lines if not line.startswith('>'))

            # Find the motif
            motif = re.compile(r'N[^P][ST][^P]')
            matches = motif.finditer(sequence)

            pos = []
            for match in matches:
                start_pos = match.start()
                pos.append(str(start_pos + 1))  # Convert positions to strings for joining

            # Only write to the output file if there are matches
            if pos:
                output_file.write(f"{code}\n{' '.join(pos)}\n")
                print(f"{code}\n{' '.join(pos)}")
            else:
                print(f"No motifs found in sequence for {code}")
        else:
            print(f"Failed to fetch data for {code1}")