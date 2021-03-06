from chromosome import Chromosome
import numpy as np
from functools import *
from genes_action import GenesAction


class GenerationFactory:

    @staticmethod
    def random_chromosomes_generator(settings):
        chromosomes_list = []
        # np.random.seed(42)
        for i in range(0, settings.CHROMOSOME_POPULATION):
            chromosome = Chromosome()
            chromosome.genes = GenesAction.generate_random_genes(settings)
            chromosome.fitness_function = settings.FF(chromosome.genes)
            chromosomes_list.append(chromosome)
        GenerationFactory._set_reproduction_probability(chromosomes_list)
        return chromosomes_list

    @staticmethod
    def search_the_most_powerful_ff(initial_population, settings):
        current_generation = initial_population[:]
        # get information from the initial population
        max_ffs = [GenerationFactory.get_highest_ff(current_generation)]
        min_ffs = [GenerationFactory.get_lowest_ff(current_generation)]
        ff_mean = [GenerationFactory.get_ff_mean(current_generation)]
        iteration = 1
        solution = None
        while (max_ffs == [] or max_ffs[-1] != settings.MAX_FF) and iteration < settings.MAX_GENERATIONS:
            # create next generation
            next_generation = GenerationFactory.create_next_generation(current_generation, settings)
            # get generation info
            max_ffs.append(GenerationFactory.get_highest_ff(next_generation))
            min_ffs.append(GenerationFactory.get_lowest_ff(next_generation))
            ff_mean.append(GenerationFactory.get_ff_mean(next_generation))
            # set new current generation
            current_generation = next_generation[:]
            # Increment iteration
            iteration += 1
        # GenerationFactory.display_chromosome(current_generation,iteration)
        if max_ffs[-1] == settings.MAX_FF:
            solution = list(map(lambda x: x.genes, list(filter(lambda x: x.fitness_function == settings.MAX_FF, current_generation))))
        return max_ffs, min_ffs, ff_mean, solution

    @staticmethod
    def create_next_generation(current_generation, settings):
        next_generation = []
        # np.random.seed(42)
        while len(next_generation) <= settings.CHROMOSOME_POPULATION - 2:
            # select chromosomes
            first_chromosome, second_chromosome = GenesAction.select_two_chromosomes(current_generation)
            # find probabilities
            crossover_prob, mut_prob = np.random.random(), np.random.random()
            # create successors from chromosomes
            new_first_chromosome = GenesAction.create_successor_from_parents((first_chromosome, second_chromosome))
            new_second_chromosome = GenesAction.create_successor_from_parents((second_chromosome, first_chromosome))
            # crossover
            if crossover_prob <= settings.CROSSOVER_PROB:
                new_first_chromosome, new_second_chromosome = GenesAction.crossover_chromosomes(new_first_chromosome, new_second_chromosome, settings)
            # mutation
            if mut_prob <= settings.MUTATION_PROB:
                new_first_chromosome, new_second_chromosome = GenesAction.mutate_chromosomes(new_first_chromosome, new_second_chromosome, settings)
            # set ff
            new_first_chromosome.fitness_function = settings.FF(new_first_chromosome.genes)
            new_second_chromosome.fitness_function = settings.FF(new_second_chromosome.genes)
            # append to the next generation
            next_generation.append(new_first_chromosome)
            next_generation.append(new_second_chromosome)
        # set reproduction prob.
        GenerationFactory._set_reproduction_probability(next_generation)
        return next_generation

    @staticmethod
    def _set_reproduction_probability(chromosomes_list):
        ff_total = reduce(lambda a, b: (a + b), map(lambda x: x.fitness_function, chromosomes_list))
        for chromosome in chromosomes_list:
            chromosome.reproduction_probability = (chromosome.fitness_function / ff_total)

    @staticmethod
    def get_highest_ff(generation):
        ff_list = list(map(lambda x: x.fitness_function, generation))
        return max(ff_list)

    @staticmethod
    def get_lowest_ff(generation):
        ff_list = list(map(lambda x: x.fitness_function, generation))
        return min(ff_list)

    @staticmethod
    def get_ff_mean(generation):
        ff_list = list(map(lambda x: x.fitness_function, generation))
        return sum(ff_list) / len(ff_list)
    # @staticmethod
    # def display_chromosome(chromosomes_list,iteration):
    #     print(f"{iteration}******************************************************************")
    #     for chromosome in chromosomes_list:
    #         print("---------------------------")
    #         print(f"FF  = {chromosome.fitness_function}")
    #         print(f"Prob  = {chromosome.reproduction_probability}")
    #         print(f"Action/s made   = {chromosome.actions_made}")
    #         print(f"Father 1 genes  = {None if chromosome.fathers is None else chromosome.fathers[0].genes}")
    #         print(f"Father 2 genes  = {None if chromosome.fathers is None else chromosome.fathers[1].genes}")
    #         print(f"Genes:            {chromosome.genes}")