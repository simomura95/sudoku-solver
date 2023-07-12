# Sudoku solver
Automatically solve sudoku using a backtracking algorithm.

The script asks the user to input the scheme, row by row. No spaces have to be inputted and 0 must be used to represent empty squares.<br>
Then, the scheme is shown to ask for confirmation; if some mistake is detected, it's possible to type it again before starting to resolve it.

The algorithm uses backtracking: starting from the top left and proceeding row by row, it tries to assing a number from 1 to 9 to each empty square, recursively.<br>
If the number can be put there, it then continues with the next square until a contradiction is detected.
When this happens, it goes back to the previous square and try the next possible number.

At the end, if a solution existed, the completed scheme is shown along with the number of backtracking steps needed.
