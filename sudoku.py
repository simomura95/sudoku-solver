class Sudoku:
    def __init__(self):
        self.table = [
            0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0,
        ]
        self.table_orig = self.table
        self.counter = 0

    def print_scheme(self, scheme):
        print()
        for r in range(9):  # row
            for c in range(0, 7, 3):  # column/group
                print(f'|{scheme[9*r + c]}.{scheme[9*r + c+1]}.{scheme[9*r + c+2]}', end='')
            print('|')
            if r in (2, 5):
                print('-------------------')

    # def print_scheme_real(self):
    #     self.print_scheme(self.table)
    #
    # def print_scheme_orig(self):
    #     self.print_scheme(self.table_orig)

    def input_scheme(self):
        print('Insert sudoku scheme row by row. Use 0 for empty spaces.')
        for i in range(9):
            correct = False
            while not correct:
                try:
                    row = input(f'Row {i + 1}: ')
                    if len(row) != 9:
                        raise ValueError
                    row_num = [int(elem) for elem in row]
                    self.table[9 * i:9 * i + 1] = row_num
                except ValueError:
                    print('Wrong Input!', end=' ')
                else:
                    correct = True
        self.table_orig = self.table

    def is_safe(self, i, num):
        row_index = i//9*9
        col_index = i % 9
        grp_index = row_index//27 * 27 + col_index//3 * 3
        if (num in self.table[row_index:row_index+9]  # row
            or num in self.table[col_index:81:9]  # column
            or num in self.table[grp_index:grp_index+3] + self.table[grp_index+9:grp_index+12] + self.table[grp_index+18:grp_index+21]):  # group
            return False
        return True

    def solve_cell(self, i):
        if i > 80:  # condizione di fine
            return True
        if self.table[i] != 0:  # se già presente numero, vado avanti
            self.counter += 1
            return self.solve_cell(i+1)
        for n in range(1, 10, 1):  # altra function(?)
            self.counter += 1
            if self.is_safe(i, n):
                self.table[i] = n
                if self.solve_cell(i + 1):
                    return True
                self.table[i] = 0
        return False  # se nessun numero va bene nella cella i, risalgo e cambio qualche numero prima


