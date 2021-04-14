from generation_factory import GenerationFactory


class Population:
    def __init__(self):
        self.chromosomes = []
        self.max_ffs = []
        self.ff_mean = []

    def create_first_generation(self):
        self.chromosomes = GenerationFactory.random_chromosomes_generator()

    def get_new_generation(self):
        self.chromosomes = GenerationFactory.create_next_generation(self.chromosomes)

    def find_the_most_powerful_chr(self):
        self.max_ffs, self.ff_mean = GenerationFactory.search_the_most_powerful_ff(self.chromosomes)
        i = 0
        for max_ff in self.max_ffs:
            print(f"Iteration {'Initial Population' if i == 0 else i}-----------------")
            print(f"Max FF: {max_ff}")
            print(f"Mean FF: {self.ff_mean[i - 1]}")
            i += 1


p = Population()
p.create_first_generation()
p.find_the_most_powerful_chr()
