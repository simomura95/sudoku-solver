from sudoku import Sudoku
import os


def cls():
    """Function to clear the console output. Works on terminal, but not in pycharm"""
    os.system('cls' if os.name == 'nt' else 'clear')


s = Sudoku()

# input scheme and ask for confirmation
s.input_scheme()
correct = ''
while correct not in ['Y', 'N']:
    cls()
    s.print_scheme(s.table)
    correct = input('Is the scheme correct? (Y/N) ').upper()
    if correct == 'N':
        cls()
        s.input_scheme()
        correct = ''

# Example scheme for test and debug
# s.table = [
#     7, 0, 4, 0, 0, 1, 2, 0, 9,
#     0, 0, 0, 0, 0, 3, 0, 0, 0,
#     8, 0, 0, 9, 0, 0, 0, 0, 5,
#     5, 6, 0, 0, 8, 0, 1, 0, 0,
#     0, 0, 0, 0, 2, 0, 0, 0, 0,
#     0, 0, 2, 0, 6, 0, 0, 9, 7,
#     9, 0, 0, 0, 0, 7, 0, 0, 6,
#     0, 0, 0, 5, 0, 0, 0, 0, 0,
#     1, 0, 3, 6, 0, 0, 4, 0, 8,
# ]

# Solve sudoku. Each check on a cell is counted
cls()
print('Starting scheme:')
s.print_scheme(s.table_orig)
if s.solve_cell(0):
    print(f'\nSolution found in {s.counter} steps: ')
    s.print_scheme(s.table)
else:
    print('Solution not found')
