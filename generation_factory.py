from chromosome import Chromosome
import numpy as np
from fitness_function_collection import FitnessFunctionCollection
from settings import Settings
from functools import *
from genes_action import GenesAction


class GenerationFactory:

    @staticmethod
    def random_chromosomes_generator():
        chromosomes_list = []
        np.random.seed(42)
        for i in range(0, Settings.CHROMOSOME_POPULATION):
            chromosome = Chromosome()
            chromosome.genes = GenesAction.generate_random_genes()
            chromosome.fitness_function = FitnessFunctionCollection.count_ones(chromosome.genes)
            chromosomes_list.append(chromosome)
        GenerationFactory._set_reproduction_probability(chromosomes_list)
        return chromosomes_list

    @staticmethod
    def search_the_most_powerful_ff(chromosomes_list):
        ff_mean = max_ffs = []
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
            first_chromosome, second_chromosome = GenesAction.select_two_chromosomes(chromosomes_list)
            crossover_prob = np.random.random(size=1)
            mut_prob = np.random.random(size=1)
            new_first_chromosome = new_second_chromosome = Chromosome()

            new_first_chromosome.fathers=(first_chromosome, second_chromosome)
            new_first_chromosome.genes = first_chromosome.genes

            new_second_chromosome.fathers=(first_chromosome, second_chromosome)
            new_second_chromosome.genes = second_chromosome.genes

            if crossover_prob <= Settings.CROSSOVER_PROB:
                new_first_chromosome, new_second_chromosome = GenesAction.crossover_chromosomes(first_chromosome,
                                                                                                second_chromosome)
            if mut_prob <= Settings.MUTATION_PROB:
                new_first_chromosome, new_second_chromosome = GenesAction.mutate_chromosomes(new_first_chromosome,
                                                                                             new_second_chromosome)
            new_first_chromosome.fitness_function = FitnessFunctionCollection.count_ones(new_first_chromosome.genes)
            new_second_chromosome.fitness_function = FitnessFunctionCollection.count_ones(new_second_chromosome.genes)
            new_chromosomes_list.append(new_first_chromosome)
            new_chromosomes_list.append(new_second_chromosome)
        GenerationFactory._set_reproduction_probability(new_chromosomes_list)
        GenerationFactory.display_chromosome(new_chromosomes_list)
        print(len(new_chromosomes_list))
        return new_chromosomes_list

    @staticmethod
    def _set_reproduction_probability(chromosomes_list):
        ff_total = reduce(lambda a, b: (a + b) * 100, map(lambda x: x.fitness_function, chromosomes_list))
        for chromosome in chromosomes_list:
            chromosome.reproduction_probability = chromosome.fitness_function / ff_total

    @staticmethod
    def display_chromosome(chromosomes_list):
        for chromosome in chromosomes_list:
            print("---------------------------")
            print(f"FF  = {chromosome.fitness_function}")
            print(f"Prob  = {chromosome.reproduction_probability}")
            print("Genes:")
            print(chromosome.genes)
