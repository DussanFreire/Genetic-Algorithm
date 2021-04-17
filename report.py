from pandas import DataFrame
import matplotlib.pyplot as pl


class Report:
    def __init__(self, max_ffs, min_ffs, mean_ffs, number_of_experiment):
        self.number_of_experiment = number_of_experiment
        self.max_ffs_for_generation = max_ffs
        self.min_ffs_for_generation = min_ffs
        self.mean_ffs_for_generation = mean_ffs
        self.number_of_generations = len(max_ffs)
        self.df_data = self.get_results_in_dataframe()

    def graficar_x_vs_y_plot(self, x_label, y_label):
        self.df_data.plot(x=x_label, y=y_label, color='red', title='scatter plot : Tip by Total bill', alpha=1)
        pl.grid()
        pl.xlabel(x_label)
        pl.ylabel(y_label)
        pl.legend()
        pl.show()

    def get_results_in_dataframe(self):
        index = ["Initial State"] + list(range(1, self.number_of_generations))
        df = DataFrame({'Generation': list(range(0, self.number_of_generations)), 'Max FF': self.max_ffs_for_generation,
                        'Min FF': self.min_ffs_for_generation, 'FF Mean': self.mean_ffs_for_generation}, index=[index])
        return df

    def display_details(self):
        print(f"Experiment:  {self.number_of_experiment}")
        print(f"Number of generations: {self.number_of_generations}")
        print(f"Max FF: {self.max_ffs_for_generation[-1]}")
        print(f"Min FF: {self.min_ffs_for_generation[-1]}")
        print(f"Mean FF: {self.mean_ffs_for_generation[-1]}")

    def display_results(self):
        self.display_details()
        pl.plot(self.df_data.loc[:, "Generation"], self.df_data.loc[:, "FF Mean"], label="Mean")
        pl.plot(self.df_data.loc[:, "Generation"], self.df_data.loc[:, "Min FF"], label="Min")
        pl.plot(self.df_data.loc[:, "Generation"], self.df_data.loc[:, "Max FF"], label="Max")
        pl.xlabel("Generation")
        pl.ylabel("Fitness function")
        pl.title("Population evolution")
        pl.grid()
        pl.legend()
        pl.show()
