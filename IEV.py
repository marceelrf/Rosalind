"""
Calculating Expected Offspring
url: http://rosalind.info/problems/iev/

Given: Six nonnegative integers, each of which does not exceed 20,000. The integers correspond to the number of couples in a population possessing each genotype pairing for a given factor. In order, the six given integers represent the number of couples having the following genotypes:
Return: The expected number of offspring displaying the dominant phenotype in the next generation, under the assumption that every couple has exactly two offspring.
"""
def offspring(x):
    offspring = (1*x[0] + 1*x[1] + 1*x[2] + 0.75*x[3] + 0.5*x[4] + 0*x[5]) * 2
    return offspring 

if __name__ == "__main__":
    with open("Datasets/rosalind_iev.txt", "r") as f:
        x = [float(i) for i in f.readline().strip().split(" ")]
    print(offspring(x))
    
offspring(x)