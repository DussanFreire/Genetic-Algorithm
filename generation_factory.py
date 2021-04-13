from chromosome import Chromosome
import numpy as np
from fitness_function_collection import FitnessFunctionCollection
from settings import Settings
from functools import *


class GenerationFactory:
    def __init__(self):
        pass

    @staticmethod
    def generation_generator(current_generation, size_expected):
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
