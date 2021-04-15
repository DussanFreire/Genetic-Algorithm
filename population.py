from generation_factory import GenerationFactory
from settings import Settings
from report import Report


class Population:
    def __init__(self):
        self.chromosomes = []
        self.setting = Settings()

    def create_first_generation(self):
        self.chromosomes = GenerationFactory.random_chromosomes_generator(self.setting)

    def find_the_most_powerful_chr(self, id):
        max_ffs, min_ffs, ff_means = GenerationFactory.search_the_most_powerful_ff(self.chromosomes, self.setting)
        generation_report = Report(max_ffs, min_ffs, ff_means, id)
        # i = 0
        # for max_ff in self.max_ffs:
        #     print(f"Iteration {'Initial Population' if i == 0 else i}-----------------")
        #     print(f"Max FF: {max_ff}")
        #     print(f"Min FF: {self.min_ffs[i - 1]}")
        #     print(f"Mean FF: {self.ff_means[i - 1]}")
        #     i += 1
        return generation_report

    def run_experiment(self):
        iteration = 0
        reports = []
        while iteration < self.setting.ITERATIONS:
            self.create_first_generation()
            reports.append(self.find_the_most_powerful_chr(iteration))
            iteration += 1
        return reports
        # 1ro ----------------------------------

# p = Population()
# reports = p.run_experiment()
# for report in reports:
#     report.display_results()
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
# p = Population()
# p.setting.CROSSOVER_PROB = 0.7
# p.create_first_generation()
# report = p.find_the_most_powerful_chr()
# df = p.get_results_in_dataframe(max_ff, min_ff, mean_ff)
# report.display_restuls()
# p.graficar_x_vs_y_plot(df, "Generation", "FF Mean")
# p.graficar_x_vs_y_plot(df, "Generation", "Min FF")
# p.graficar_x_vs_y_plot(df, "Generation", "Max FF")
