from chromosome import Chromosome
import numpy as np
from fitness_function_collection import FitnessFunctionCollection
from settings import Settings
from functools import *
import random


class GenerationFactory:

    @staticmethod
    def random_chromosomes_generator():
        chromosomes_list = []
        np.random.seed(42)
        for i in range(0, Settings.CHROMOSOME_POPULATION):
            chromosome = Chromosome()
            chromosome.genes = GenerationFactory._generate_random_genes()
            chromosome.fitness_function = FitnessFunctionCollection.count_ones(chromosome.genes)
            chromosomes_list.append(chromosome)
        GenerationFactory._set_reproduction_probability(chromosomes_list)
        return chromosomes_list

    @staticmethod
    def search_the_most_powerfull_chr(chromosomes_list):
        max_ffs = []
        ff_mean = []
        iteration = 0
        while iteration < Settings.ITERATIONS and (max_ffs == [] or max_ffs[-1] != Settings.MAX_FF):
            new_chromosomes_list = GenerationFactory.create_next_generation(chromosomes_list)
            ff_list = list(map(lambda x: x.fitness_function, new_chromosomes_list))
            max_ffs.append(max(ff_list))
            ff_mean.append(sum(ff_list) / len(ff_list))
            iteration += 1
        return max_ffs, ff_mean

    @staticmethod
    def create_next_generation(chromosomes_list):
        new_chromosomes_list = []
        np.random.seed(42)
        while len(new_chromosomes_list) <= Settings.CHROMOSOME_POPULATION:
            first_chromosome, second_chromosome = GenerationFactory._select_two_chromosomes(chromosomes_list)
            crossover_prob = np.random.random(size=1)
            mut_prob = np.random.random(size=1)
            if crossover_prob <= Settings.CROSSOVER_PROB:
                first_chromosome, second_chromosome = GenerationFactory._crossover_chromosomes(first_chromosome, second_chromosome)
                # print(f"Cr1 = {first_chromosome.genes}; Cr2 = {second_chromosome.genes}")
            if mut_prob <= Settings.MUTATION_PROB:
                first_chromosome, second_chromosome = GenerationFactory._mutate_chromosomes(first_chromosome, second_chromosome)
            first_chromosome.fitness_function = FitnessFunctionCollection.count_ones(first_chromosome.genes)
            second_chromosome.fitness_function = FitnessFunctionCollection.count_ones(second_chromosome.genes)
            new_chromosomes_list.append(first_chromosome)
            new_chromosomes_list.append(second_chromosome)
        GenerationFactory._set_reproduction_probability(new_chromosomes_list)
        return new_chromosomes_list

    @staticmethod
    def _generate_random_genes():
        random_genes = np.random.random(size=Settings.NUMBER_GENES)
        random_genes = [int(round(num, 0)) for num in random_genes] * Settings.HIGHER_GENE
        return random_genes

    @staticmethod
    def _set_reproduction_probability(chromosomes_list):
        ff_total = reduce(lambda a, b: a + b, map(lambda x: x.fitness_function, chromosomes_list))
        for chromosome in chromosomes_list:
            chromosome.reproduction_probability = chromosome.fitness_function / ff_total

    @staticmethod
    def _select_two_chromosomes(chromosomes):
        first_chr = second_chr = None
        # print(list(map(lambda c: c.reproduction_probability * 100, chromosomes)))
        while first_chr == second_chr:
            first_chr, second_chr = random.choices(chromosomes, weights=(list(map(lambda c: c.reproduction_probability * 100, chromosomes))), k=2)
        return first_chr, second_chr

    @staticmethod
    def _crossover_chromosomes(first_chromosome, second_chromosome):
        gene_index = int(round(np.random.random(size=1)[0] * Settings.NUMBER_GENES, 0))
        # print("Cross over----------------")
        # print(f"Cr1 = {first_chromosome.genes}; Cr2 = {second_chromosome.genes}; Indice = {gene_index}")
        first_chr_mutation = second_chromosome.genes[gene_index:]
        second_chr_mutation = first_chromosome.genes[gene_index:]
        first_chromosome.genes[gene_index:] = first_chr_mutation
        second_chromosome.genes[gene_index:] = second_chr_mutation
        # print(f"Cr1 = {first_chromosome.genes}; Cr2 = {second_chromosome.genes}")
        return first_chromosome, second_chromosome

    @staticmethod
    def _mutate_chromosomes(first_chromosome, second_chromosome):
        gene_index = int(round(np.random.random(size=1)[0] * Settings.NUMBER_GENES, 0)) + 1
        # print("Mutation----------------")
        # print(f"Cr1 = {first_chromosome.genes}; Cr2 = {second_chromosome.genes}; Indice = {gene_index}")
        first_chromosome.genes[gene_index] = first_chromosome.genes[gene_index] + 1 if first_chromosome.genes[gene_index] < Settings.HIGHER_GENE else first_chromosome.genes[gene_index] - 1
        second_chromosome.genes[gene_index] = second_chromosome.genes[gene_index] + 1 if second_chromosome.genes[gene_index] < Settings.HIGHER_GENE else second_chromosome.genes[gene_index] - 1
        # print(f"Cr1 = {first_chromosome.genes}; Cr2 = {second_chromosome.genes}")
        return first_chromosome, second_chromosome
