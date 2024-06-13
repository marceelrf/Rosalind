def generate_kmers(sequence, k):
    """
    Gera todos os k-mers de uma sequência de DNA ou RNA.

    Parâmetros:
    sequence (str): A sequência de DNA ou RNA.
    k (int): O comprimento dos k-mers.

    Retorna:
    list: Uma lista contendo todos os k-mers da sequência.
    """
    kmers = [sequence[i:i+k] for i in range(len(sequence) - k + 1)]
    return kmers