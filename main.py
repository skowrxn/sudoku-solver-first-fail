import argparse
from enum import Enum
from src.solvers.naive_solver import NaiveSolver
from src.solvers.first_fail_solver import FirstFailSolver
from src.solvers.dancing_links_solver import DancingLinksSolver


class SudokuSolverType(Enum):
    naive = 'naive'
    first_fail = 'first_fail' 
    dancing_links = 'dancing_links'


def get_solver(solver_type):
    if solver_type == SudokuSolverType.naive:
        return NaiveSolver
    elif solver_type == SudokuSolverType.first_fail:
        return FirstFailSolver
    elif solver_type == SudokuSolverType.dancing_links:
        return DancingLinksSolver
    return NaiveSolver

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
    
    solver_class = get_solver(args.algorithm)
    solver = solver_class(time_limit=args.time_limit)
    solver.run(args.puzzle_path)


if __name__ == "__main__":
    main()