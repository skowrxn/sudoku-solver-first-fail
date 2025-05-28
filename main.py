import argparse
from enum import Enum

from src.model.grid import SudokuGrid
from src.solvers.dancing_links_solver import DancingLinksSudokuSolver
from src.solvers.first_fail_solver import FirstFailSudokuSolver
from src.solvers.naive_solver import NaiveSudokuSolver


class SudokuSolverType(Enum):
    naive = 'naive'
    first_fail = 'first_fail' 
    dancing_links = 'dancing_links'


def main():
    parser = argparse.ArgumentParser(
        prog='sudolver',
        description='Sudolver - yet another sudoku solver.'
    )
    parser.add_argument('puzzle_path', help='path to the file containing a sudoku puzzle')
    parser.add_argument('--algorithm', '-a', 
                       type=SudokuSolverType,
                       choices=list(SudokuSolverType),
                       help='algorithm used to solver the sudoku')
    parser.add_argument('--time-limit', '-t',
                       type=float,
                       help='time limit for the solver (in seconds)')
    args = parser.parse_args()

    with open(args.puzzle_path, 'r') as file:
        grid = SudokuGrid.from_text(file.readlines())
        match args.algorithm:
            case SudokuSolverType.naive:
                result = NaiveSudokuSolver(grid, args.time_limit).solve(grid, args.time_limit)
                if result is None:
                    return 1
                print(result.__str__())
            case SudokuSolverType.first_fail:
                result = FirstFailSudokuSolver(grid, args.time_limit).solve(grid, args.time_limit)
                if result is None:
                    return 1
                print(result.__str__())
            case SudokuSolverType.dancing_links:
                result = DancingLinksSudokuSolver(grid, args.time_limit).solve(grid, args.time_limit)
                if result is None:
                    return 1
                print(result.__str__())
        return 0


if __name__ == "__main__":
    main()