from generation_factory import GenerationFactory
from settings import Settings
from report import Report
import numpy as np


class Population:
    def __init__(self):
        self.chromosomes = []
        self.setting = Settings()

    def create_first_generation(self):
        self.chromosomes = GenerationFactory.random_chromosomes_generator(self.setting)

    def find_the_most_powerful_chr(self, number_of_experiment):
        max_ffs, min_ffs, ff_means = GenerationFactory.search_the_most_powerful_ff(self.chromosomes, self.setting)
        generation_report = Report(max_ffs, min_ffs, ff_means, number_of_experiment)
        return generation_report

    def run_experiment(self):
        iteration = 0
        reports = []
        np.random.seed(47)
        while iteration < self.setting.NUMBER_OF_EXPERIMENTS:
            self.create_first_generation()
            reports.append(self.find_the_most_powerful_chr(iteration))
            iteration += 1
        return reports
#
#.

def display_best_experiment(exp_reports):
    min_number_of_generation = min(list(map(lambda r: r.number_of_generations, exp_reports)))
    report_with_less_generations = list(filter(lambda r: r.number_of_generations ==min_number_of_generation,exp_reports ))
    for report in report_with_less_generations:
        report.display_results()

p_10 = Population()
p_10.setting.MAX_GENERATIONS = 1000
p_10.setting.CHROMOSOME_POPULATION = 300
p_10.setting.CROSSOVER_PROB = 0.8
p_10.setting.MUTATION_PROB = 0.005
p_10.setting.set_fitness_function("all ones")
p_10.setting.NUMBER_OF_EXPERIMENTS = 1
reports_10 = p_10.run_experiment()
display_best_experiment(reports_10)