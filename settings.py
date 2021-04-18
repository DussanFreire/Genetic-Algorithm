from fitness_function_collection import FitnessFunctionCollection


class Settings:
    def __init__(self):
        self.HIGHEST_GENE_VALUE = 1
        self.NUMBER_OF_EXPERIMENTS = 20
        self.NUMBER_GENES = 20
        self.CHROMOSOME_POPULATION = 100
        self.CROSSOVER_PROB = 0.7
        self.MUTATION_PROB = 0.001
        self.MAX_FF = 20
        self.MAX_GENERATIONS = 1000
        self.FF = FitnessFunctionCollection.count_ones

    def set_fitness_function(self, fitness_function):
        if "count ones" == fitness_function:
            self.FF = FitnessFunctionCollection.count_ones
            self.MAX_FF = 20
            self.HIGHEST_GENE_VALUE = 1
        elif "all ones" == fitness_function:
            self.FF = FitnessFunctionCollection.all_ones
            self.MAX_FF = 38400
            self.HIGHEST_GENE_VALUE = 9
        elif "queens in peace" == fitness_function:
            self.FF = FitnessFunctionCollection.queens_in_peace
            self.MAX_FF = 28
            self.HIGHEST_GENE_VALUE = 7
            self.NUMBER_GENES = 8
