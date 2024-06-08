def protein_MW(sequence):
    """
    Calcula a massa molecular de uma proteína com base na sua sequência de aminoácidos.

    Args:
        sequence (str): Uma string representando a sequência de aminoácidos, onde cada aminoácido é representado
                        pelo seu código de uma letra.

    Returns:
        float: A massa molecular total da proteína.

    Exemplo:
        >>> amino_acid_masses = {
                "A": 71.03711, "C": 103.00919, "D": 115.02694, "E": 129.04259,
                "F": 147.06841, "G": 57.02146, "H": 137.05891, "I": 113.08406,
                "K": 128.09496, "L": 113.08406, "M": 131.04049, "N": 114.04293,
                "P": 97.05276, "Q": 128.05858, "R": 156.10111, "S": 87.03203,
                "T": 101.04768, "V": 99.06841, "W": 186.07931, "Y": 163.06333
            }
        >>> protein_MW("ACDEFGHIKLMNPQRSTVWY")
        2395.73611
    """
    
    amino_acid_masses = {
    "A": 71.03711,
    "C": 103.00919,
    "D": 115.02694,
    "E": 129.04259,
    "F": 147.06841,
    "G": 57.02146,
    "H": 137.05891,
    "I": 113.08406,
    "K": 128.09496,
    "L": 113.08406,
    "M": 131.04049,
    "N": 114.04293,
    "P": 97.05276,
    "Q": 128.05858,
    "R": 156.10111,
    "S": 87.03203,
    "T": 101.04768,
    "V": 99.06841,
    "W": 186.07931,
    "Y": 163.06333
    }
    
    mass = 0
    
    for i in range(0,len(sequence)):
        mass = mass + amino_acid_masses.get(sequence[i])
        
    return mass