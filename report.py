from pandas import DataFrame
import matplotlib.pyplot as pl


def _get_results_in_dataframe(max_ffs, min_ff, ff_means):
    index = ["Initial State"] + list(range(1, len(max_ffs)))
    df = DataFrame(
        {'Generation': list(range(0, len(max_ffs))), 'Max FF': max_ffs, 'Min FF': min_ff, 'FF Mean': ff_means},
        index=[index])
    return df


class Report:
    def __init__(self, max_ffs, min_ffs, mean_ffs, id):
        self.number_of_experiment = id
        self.max_ffs_for_generation = max_ffs
        self.min_ffs_for_generation = min_ffs
        self.mean_ffs_for_generation = mean_ffs
        self.df_data = _get_results_in_dataframe(max_ffs, min_ffs, mean_ffs)
        self.number_of_generations = len(max_ffs)

    def graficar_x_vs_y_plot(self, xlabel, ylabel):
        self.df_data.plot(x=xlabel, y=ylabel, color='red', title='scatter plot : Tip by Total bill', alpha=1)
        pl.grid()
        pl.xlabel(xlabel)
        pl.ylabel(ylabel)
        pl.legend()
        pl.show()

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
