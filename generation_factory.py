from chromosome import Chromosome

class GenerationFactory:
    def __init__(self):
        pass

    @staticmethod
    def generarion_generator(size_expected):
        chromosomes_list = []
        for i in range(0, size_expected):
            new_chromosome = Chromosome()
            new_chromosome.genes = random_genes
            new_chromosome.fitness_function = fitness_function(chr.genes)
            chromosomes_list.append(chr)
        set_reproduction_probability(chromosomes_list)
        return chromosomes_list


