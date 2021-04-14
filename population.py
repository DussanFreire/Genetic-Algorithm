from generation_factory import GenerationFactory
from pandas import DataFrame
import matplotlib.pyplot as pl
import seaborn as sns


class Population:
    def __init__(self):
        self.chromosomes = []
        self.max_ffs = []
        self.ff_means = []

    def create_first_generation(self):
        self.chromosomes = GenerationFactory.random_chromosomes_generator()

    def get_new_generation(self):
        self.chromosomes = GenerationFactory.create_next_generation(self.chromosomes)

    def find_the_most_powerful_chr(self):
        self.max_ffs, self.ff_means = GenerationFactory.search_the_most_powerful_ff(self.chromosomes)
        i = 0
        for max_ff in self.max_ffs:
            print(f"Iteration {'Initial Population' if i == 0 else i}-----------------")
            print(f"Max FF: {max_ff}")
            print(f"Mean FF: {self.ff_means[i - 1]}")
            i += 1
        return self.max_ffs, self.ff_means

    def get_results_in_dataframe(self, max_ffs, ff_means):
        index = ["Initial State"] + list(range(1, len(max_ffs)))
        df = DataFrame({'Generation': list(range(0, len(max_ffs))), 'Max FF': max_ffs, 'FF Mean': ff_means},
                       index=[index])
        return df

    def graficar_x_vs_y(self, df, xlabel, ylabel):
        df.plot(x=xlabel, y=ylabel, color='red', title='scatter plot : Tip by Total bill', alpha=1)
        pl.grid()
        pl.xlabel(xlabel)
        pl.ylabel(ylabel)
        pl.legend()
        pl.show()


p = Population()
p.create_first_generation()
max_ff, mean_ff = p.find_the_most_powerful_chr()
df = p.get_results_in_dataframe(max_ff, mean_ff)
p.graficar_x_vs_y(df, "Generation", "FF Mean")
p.graficar_x_vs_y(df, "Generation", "Max FF")
