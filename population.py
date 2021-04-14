from generation_factory import GenerationFactory
from pandas import DataFrame
from settings import Settings
import matplotlib.pyplot as pl
import seaborn as sns


class Population:
    def __init__(self):
        self.chromosomes = []
        self.setting = Settings()
        self.max_ffs = []
        self.min_ffs = []
        self.ff_means = []

    def create_first_generation(self):
        self.chromosomes = GenerationFactory.random_chromosomes_generator()

    def get_new_generation(self):
        self.chromosomes = GenerationFactory.create_next_generation(self.chromosomes)

    def find_the_most_powerful_chr(self):
        self.max_ffs, self.min_ffs, self.ff_means = GenerationFactory.search_the_most_powerful_ff(self.chromosomes)
        i = 0
        for max_ff in self.max_ffs:
            print(f"Iteration {'Initial Population' if i == 0 else i}-----------------")
            print(f"Max FF: {max_ff}")
            print(f"Min FF: {self.min_ffs[i - 1]}")
            print(f"Mean FF: {self.ff_means[i - 1]}")
            i += 1
        return self.max_ffs, self.min_ffs, self.ff_means

    def get_results_in_dataframe(self, max_ffs, min_ff, ff_means):
        index = ["Initial State"] + list(range(1, len(max_ffs)))
        df = DataFrame(
            {'Generation': list(range(0, len(max_ffs))), 'Max FF': max_ffs, 'Min FF': min_ff, 'FF Mean': ff_means},
            index=[index])
        return df

    def graficar_x_vs_y_plot(self, df, xlabel, ylabel):
        df.plot(x=xlabel, y=ylabel, color='red', title='scatter plot : Tip by Total bill', alpha=1)
        pl.grid()
        pl.xlabel(xlabel)
        pl.ylabel(ylabel)
        pl.legend()
        pl.show()

    def display_restuls(self, df):
        pl.plot(df.loc[:, "Generation"], df.loc[:, "FF Mean"], label="Mean")
        pl.plot(df.loc[:, "Generation"], df.loc[:, "Min FF"], label="Min")
        pl.plot(df.loc[:, "Generation"], df.loc[:, "Max FF"], label="Max")
        pl.xlabel("Generation")
        pl.ylabel("Fitness function")
        pl.title("Population evolution")
        pl.grid()
        pl.legend()
        pl.show()

# 1ro ----------------------------------
# experimentar 20 veces
# pc = 0.7
# pm = 0.001
# 20 genes
# 100 cromosomas
# 2do ----------------------------------
# experimentar 20 veces
# pc = 0
# pm = 0.7
# 20 genes
# 100 cromosomas
# 3er ----------------------------------
# experimentar 20 veces
# pc = 0.7
# pm = 0
# 20 genes
# 100 cromosomas
# 4to ----------------------------------
# experimentar 20 veces
# pc = 0.9
# pm = 0.001
# 20 genes
# 100 cromosomas
# 5to ----------------------------------
# experimentar 20 veces
# pc = 0.3
# pm = 0.001
# 20 genes
# 100 cromosomas
# ¿Cu´al es la mejor opci´on de par´ametros seg´un los resultados obtenidos anteriormente? ¿Por qu´e?p = Population()
p = Population
p.create_first_generation()
max_ff, min_ff, mean_ff = p.find_the_most_powerful_chr()
df = p.get_results_in_dataframe(max_ff, min_ff, mean_ff)
p.display_restuls(df)
# p.graficar_x_vs_y_plot(df, "Generation", "FF Mean")
# p.graficar_x_vs_y_plot(df, "Generation", "Min FF")
# p.graficar_x_vs_y_plot(df, "Generation", "Max FF")
