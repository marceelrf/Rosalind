from Bio import SeqIO

Sequence = list(SeqIO.parse("Datasets/test_LONG.txt","fasta"))

len(Sequence)

def get_overlap_string(s1,s2):
    combine_strings = []
    overlap_strings = []
    
    #Busca por substrings em comum
    for i in range(len(s1)):
        
        if s1[i:] == s2[:len(s1)-1]:
            overlap_strings.append(s1[i:])
            combine_strings.append(s1+s2[len(s1)-i:])
            break
    for i in range(len(s2)):
        if s2[i:] == s1[:len(s2)-i]:
            overlap_strings.append(s2[i:])
            combine_strings.append(s2+s1[len(s2)-i:])
            break
        
    if not overlap_strings:
        return "", ""    
    
    combine_string = min(combine_strings, key=len)
    overlap_string = max(overlap_strings, key=len)
    
    return combine_string, overlap_string

get_overlap_string(str(Sequence[2].seq),str(Sequence[0].seq))

# def find_superstring(strings):
#     temp = strings[:]

#     while len(temp) > 1:
#         most_overlapping_string = ""
#         most_overlapping_string_pair = []
#         most_overlapping_string_length = 0

#         for i in range(len(temp) - 1):
#             for j in range(i + 1, len(temp)):
#                 combine_string, overlap_string = get_overlap_string(temp[i], temp[j])
#                 if len(overlap_string) > most_overlapping_string_length:
#                     most_overlapping_string = combine_string
#                     most_overlapping_string_pair = [temp[i], temp[j]]
#                     most_overlapping_string_length = len(overlap_string)

#         temp.remove(most_overlapping_string_pair[0])
#         temp.remove(most_overlapping_string_pair[1])
#         temp.append(most_overlapping_string)

#     return temp[0]


for i in range(len(Sequence)):
    

if __name__ == "__main__":
    # load data
    seq_name, seq_string = [], []
    with open ("Datasets/test_LONG.txt",'r') as fa:
        for seq_record in SeqIO.parse(fa,'fasta'):
            seq_name.append(str(seq_record.name))
            seq_string.append(str(seq_record.seq))
    shortest_superstring = find_superstring(seq_string)
    print(shortest_superstring)