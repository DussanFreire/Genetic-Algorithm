import numpy as np
import random
from chromosome import Chromosome


class GenesAction:
    @staticmethod
    def select_two_chromosomes(chromosomes):
        first_chr = None
        second_chr = None
        while first_chr == second_chr:
            first_chr, second_chr = random.choices(chromosomes, weights=(
                list(map(lambda c: c.reproduction_probability, chromosomes))), k=2)
        return first_chr, second_chr

    @staticmethod
    def crossover_chromosomes(first_chromosome, second_chromosome, settings):
        # The start of the range is chosen
        gene_index = int(round(np.random.random(size=1)[0] * settings.NUMBER_GENES, 0)) - 1
        # A copy of the input chromosomes is made in order to switch the chromosomes
        first_chr_genes = first_chromosome.genes[:]
        second_chr_genes = second_chromosome.genes[:]
        # crossover action is saved in the chromosome, this step is used only to debug
        first_chromosome.actions_made.append(f"Crossover, index: {gene_index}")
        second_chromosome.actions_made.append(f"Crossover, index: {gene_index}")
        # The witch is made
        first_chromosome.genes = first_chr_genes[:gene_index] + second_chr_genes[gene_index:]
        second_chromosome.genes = second_chr_genes[:gene_index] + first_chr_genes[gene_index:]
        # return both chromosomes
        return first_chromosome, second_chromosome

    @staticmethod
    def mutate_chromosomes(first_chromosome, second_chromosome, settings):
        # A gene is chosen
        gene_index = int(round(np.random.random(size=1)[0] * settings.NUMBER_GENES, 0)) - 1
        # mutation action is saved in the chromosome, this step is used only to debug
        first_chromosome.actions_made.append(f"Mutation, index: {gene_index}")
        second_chromosome.actions_made.append(f"Mutation, index: {gene_index}")
        # The mutation starts, if the chosen gene has a value lower than the highest gene, then its value increment,
        # otherwise it decrease
        first_chromosome.genes[gene_index] = first_chromosome.genes[gene_index] + 1 if first_chromosome.genes[gene_index] < settings.HIGHEST_GENE_VALUE else first_chromosome.genes[gene_index] - 1
        second_chromosome.genes[gene_index] = second_chromosome.genes[gene_index] + 1 if second_chromosome.genes[gene_index] < settings.HIGHEST_GENE_VALUE else second_chromosome.genes[gene_index] - 1
        # return both chromosomes
        return first_chromosome, second_chromosome

    @staticmethod
    def generate_random_genes(settings):
        random_genes = np.random.random(size=settings.NUMBER_GENES)
        random_genes = [int(round(num, 0)) for num in random_genes * settings.HIGHEST_GENE_VALUE]
        return random_genes

    @staticmethod
    def create_successor_from_parents(parents):
        # This part is only required in order to debug
        new_first_chromosome = Chromosome()
        new_first_chromosome.fathers = parents
        new_first_chromosome.genes = parents[0].genes[:]
        return new_first_chromosome
