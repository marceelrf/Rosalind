from Bio import SeqIO
import numpy as np


records = list(SeqIO.parse("Datasets/rosalind_cons.txt", "fasta"))

len(records)


A_count = np.zeros(len(str(records[1].seq)))
T_count = np.zeros(len(str(records[1].seq)))
C_count = np.zeros(len(str(records[1].seq)))
G_count = np.zeros(len(str(records[1].seq)))

for i in range(0,len(records)):
    print(records[i].id)
    
    
    # for j in str(records[i].seq):
    for j in range(0,len(str(records[i].seq))):
        print(str(records[i].seq)[j])
        
        if str(records[i].seq)[j] == "A":
            A_count[j] = A_count[j] + 1
        if str(records[i].seq)[j] == "T":
            T_count[j] = T_count[j] + 1
        if str(records[i].seq)[j] == "C":
            C_count[j] = C_count[j] + 1
        if str(records[i].seq)[j] == "G":
            G_count[j] = G_count[j] + 1
 

# Stack arrays vertically to compare elements at each position
stacked_arrays = np.vstack([A_count, C_count, G_count, T_count])
stacked_arrays
# Get the index of the array with the maximum value at each position
max_indices = np.argmax(stacked_arrays, axis=0)
max_indices

# List of array names
array_names = ['A', 'C', 'G', 'T']

# Get the names of the arrays with the maximum values at each position
max_array_names = [array_names[idx] for idx in max_indices]
max_array_names

max_array_names_string = ''.join(max_array_names)
max_array_names_string


A_count
T_count
C_count
G_count

A_count_str = ' '.join(map(str, A_count.tolist()))
C_count_str = ' '.join(map(str, C_count.tolist()))
G_count_str = ' '.join(map(str, G_count.tolist()))
T_count_str = ' '.join(map(str, T_count.tolist()))

output_string = f"{max_array_names_string}\nA: {A_count_str}\nC: {C_count_str}\nG: {G_count_str}\nT: {T_count_str}"

# Save the output to a text file
with open("Output/CONS.txt", "w") as file:
    file.write(output_string)