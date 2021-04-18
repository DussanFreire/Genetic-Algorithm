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

    @staticmethod
    def queens_in_peace(cols):
        ff = 0
        for col in range(0, len(cols)):
            if col == len(cols) - 1:
                break
            diagonal_sup = cols[col] + col
            diagonal_inf = cols[col] - col
            for col_aux in range(col + 1, len(cols)):
                diagonal_sup_aux = cols[col_aux] + col_aux
                diagonal_inf_aux = cols[col_aux] - col_aux
                if diagonal_sup_aux == diagonal_sup:
                    continue
                if diagonal_inf_aux == diagonal_inf:
                    continue
                if cols[col] == cols[col_aux]:
                    continue
                ff += 1
        return ff

