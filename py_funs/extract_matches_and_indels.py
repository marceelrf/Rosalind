import re

def extract_matches_and_indels(sequence, cigar):
    """
    Extract regions with matches (M), insertions (I), and deletions (D) from a read sequence using a CIGAR string.

    :param sequence: The read sequence (a string).
    :param cigar: The CIGAR string (a string).
    :return: A string containing only the regions with matches and InDels.
    """
    pattern = re.compile(r'(\d+)([MIDNSHP=X])')
    matches = pattern.findall(cigar)

    result = []
    seq_index = 0

    for length, op in matches:
        length = int(length)
        if op == 'M' or op == '=' or op == 'X':  # Match
            result.append(sequence[seq_index:seq_index + length])
            seq_index += length
        elif op == 'I':  # Insertion to the reference
            result.append(sequence[seq_index:seq_index + length])
            seq_index += length
        elif op == 'D':  # Deletion from the reference
            result.append('-' * length)
        elif op in 'NSHP':  # Skip, soft clipping, hard clipping, padding
            if op == 'S' or op == 'H':  # Soft clipping, hard clipping
                seq_index += length

    return ''.join(result)

# Example usage:
sequence = "ACTGACTGACTG"
cigar = "4M2I3M2D3M"
result = extract_matches_and_indels(sequence, cigar)
print(result)  # Output should be "ACTGACTGACTG--ACTG"
