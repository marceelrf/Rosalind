def find_shortest_sequence_in_array(sequences):
    """
    Retorna a sequência de menor tamanho em um array de sequências de DNA.

    Parâmetros:
    sequences (list): Uma lista de strings representando sequências de DNA.

    Retorna:
    str: A sequência de menor tamanho.
    """
    if not sequences:
        return None  # Retorna None se o array estiver vazio

    shortest_sequence = min(sequences, key=len)
    return shortest_sequence