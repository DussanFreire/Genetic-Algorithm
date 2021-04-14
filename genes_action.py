import numpy as np
from settings import Settings
import random
from chromosome import Chromosome

class GenesAction:
    @staticmethod
    def select_two_chromosomes(chromosomes):
        first_chr = second_chr = None
        # print(list(map(lambda c: c.reproduction_probability * 100, chromosomes)))
        while first_chr == second_chr:
            first_chr, second_chr = random.choices(chromosomes, weights=(
                list(map(lambda c: c.reproduction_probability, chromosomes))), k=2)
        return first_chr, second_chr

    @staticmethod
    def crossover_chromosomes(first_chromosome, second_chromosome):
        gene_index = int(round(np.random.random(size=1)[0] * Settings.NUMBER_GENES, 0))
        new_first_chr = new_second_chr = Chromosome()
        new_first_chr.genes = first_chromosome.genes[:gene_index] + second_chromosome.genes[gene_index:]
        new_second_chr.genes = second_chromosome.genes[:gene_index] + first_chromosome.genes[gene_index:]
        return new_first_chr, new_second_chr

    @staticmethod
    def mutate_chromosomes(first_chromosome, second_chromosome):
        gene_index = int(round(np.random.random(size=1)[0] * Settings.NUMBER_GENES, 0)) + 1
        # print("Mutation----------------")
        # print(f"Cr1 = {first_chromosome.genes}; Cr2 = {second_chromosome.genes}; Indice = {gene_index}")
        first_chromosome.genes[gene_index] = first_chromosome.genes[gene_index] + 1 if first_chromosome.genes[
                                                                                           gene_index] < Settings.HIGHER_GENE else \
            first_chromosome.genes[gene_index] - 1
        second_chromosome.genes[gene_index] = second_chromosome.genes[gene_index] + 1 if second_chromosome.genes[
                                                                                             gene_index] < Settings.HIGHER_GENE else \
            second_chromosome.genes[gene_index] - 1
        # print(f"Cr1 = {first_chromosome.genes}; Cr2 = {second_chromosome.genes}")
        return first_chromosome, second_chromosome

    @staticmethod
    def generate_random_genes():
        random_genes = np.random.random(size=Settings.NUMBER_GENES)
        random_genes = [int(round(num, 0)) for num in random_genes] * Settings.HIGHER_GENE
        return random_genes

