class FitnessFunctionCollection:

    @staticmethod
    def count_ones(genes):
        return genes.count(1)

    @staticmethod
    def all_ones(genes):
        aux = 0
        for gene in genes:
            if gene == 1:
                aux += 1920
            elif gene == 0 or gene == 2:
                aux += 960
            elif gene == 3:
                aux += 480
            elif gene == 4:
                aux += 240
            elif gene == 5:
                aux += 120
            elif gene == 6:
                aux += 60
            elif gene == 7:
                aux += 30
            elif gene == 8:
                aux += 10
            elif gene == 9:
                aux += 0
        return aux
