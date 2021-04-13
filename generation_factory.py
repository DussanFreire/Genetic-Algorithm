from chromosome import Chromosome
import numpy as np
from fitness_function_collection import FitnessFunctionCollection
from settings import Settings
from functools import *
import random


class GenerationFactory:

    @staticmethod
    def chromosomes_generator(current_generation, size_expected):
        chromosomes_list = []
        for i in range(0, size_expected):
            chromosome = Chromosome()
            chromosome.genes = GenerationFactory.generate_random_genes
            chromosome.fitness_function = FitnessFunctionCollection.count_ones(chromosome.genes)
            chromosomes_list.append(chromosome)
        GenerationFactory.set_reproduction_probability(chromosomes_list)
        return chromosomes_list

    @staticmethod
    def generate_random_genes():
        np.random.seed(42)
        random_genes = np.random.random(size=Settings.NUMBER_GENES)
        random_genes = [round(num, 1) for num in random_genes]
        return random_genes

    @staticmethod
    def set_reproduction_probability(chromosomes_list):
        ff_total = reduce(lambda a, b: a.fitness_function + b.fitness_function, chromosomes_list)
        for chromosome in chromosomes_list:
            chromosome.reproduction_probability = chromosome.fitness_function / ff_total

    @staticmethod
    def select_two_chromosomes(chromosomes):
        first_chr = second_chr = None
        while first_chr == second_chr:
            first_chr, second_chr = random.choices(chromosomes, weights=(
                [chromosome.reproduction_probability for chromosome in chromosomes]), k=2)
        return first_chr, second_chr

    @staticmethod
    def crossover_chromosomes(first_chromosome, second_chromosome, number_of_genes=3):
        first_chr_mutation = second_chromosome.genes[-number_of_genes]
        second_chr_mutation = first_chromosome.genes[-number_of_genes]
        first_chromosome.genes[-number_of_genes] = first_chr_mutation
        second_chromosome.genes[-number_of_genes] = second_chr_mutation
        return first_chromosome, second_chromosome

    @staticmethod
    def mutate_chromosomes(first_chromosome, second_chromosome, number_of_genes=3):
        gene_index = np.random.random(size=1) * number_of_genes
        aux = first_chromosome.genes[gene_index]
        first_chromosome.genes[gene_index] = second_chromosome.genes[gene_index]
        second_chromosome.genes[gene_index] = aux
        return first_chromosome, second_chromosome

