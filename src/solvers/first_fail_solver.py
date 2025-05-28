from __future__ import annotations
from dataclasses import dataclass
from typing import NewType
from src.solvers.solver import SudokuSolver
from src.model.grid import SudokuGrid
from src.utils.recursion_limit import recursion_limit_set_to  # noqa


Variable = NewType("Variable", tuple[int, int, int])
"""Type representing a single variable identifier, it's a tuple with
   the variable's coordinates (row index, col index, block index)"""

Domain = NewType("Domain", set[int])
"""Type representing set of of available values"""


@dataclass(frozen=True, slots=True)
class State:
    """
    Represent the current state of the backtracking solver.

    Attributes:
    -----------
    grid: SudokuGrid
        a current state of the grid
    free_variables: set[Variable]
        set of the variables without assigned values
    row_domains: list[Domain]
        set of values available in the given row, e.g.
            row_domains[5] = {1,2,3,4}
        means the {1,2,3,4} can be assigned in row 5
    col_domains: list[Domain]
        set of values available in the given column
    block_domains: list[Domain]
        set of values available in the given block
    """

    grid: SudokuGrid
    free_variables: set[Variable]
    row_domains: list[Domain]
    col_domains: list[Domain]
    block_domains: list[Domain]

    def domain(self, variable: Variable) -> Domain:
        """
        Return domain (available values) for the given variable.

        Parameters:
        -----------
        variable: Variable
            a variable whose domain we want to get


        Return:
        --------
        domain: Domain
            values available for the given domain
        """


        # TODO:
        # Implement the method as described in the docstring.
        #
        # tip 1. read Variable type documentation
        # tip 2. use self.row_domains, self.col_domains, self.block_domains
        # tip 3. docs: https://docs.python.org/3.13/library/stdtypes.html#set.intersection
        raise NotImplementedError("not implemented — remove this line")

    def assign(self, variable: Variable, value: int) -> None:
        """
        Assigns a given value to a given variable.

        Parameters:
        -----------
        variable: Variable
            variable to be assigned to
        value: int
            what value should we assign
        """
        # TODO:
        # Update the state according to the docstring
        # tip. you need to modify:
        #   - self.grid
        #   - self.free_variables
        #   - self.row_domains
        #   - self.col_domains
        #   - self.block_domains
        raise NotImplementedError("not implemented — remove this line")

    def remove_assignment(self, variable: Variable) -> None:
        """
        Removes a value assignment.

        Parameters:
        -----------
        variable: Variable
            an already assigned variable
        """
        # TODO:
        # Update the state according to the docstring.
        # tip 1. you need to modify:
        #   - self.grid
        #   - self.free_variables
        #   - self.row_domains
        #   - self.col_domains
        #   - self.block_domains
        #
        # tip 2. grid contains the current value
        raise NotImplementedError("not implemented — remove this line")

    @staticmethod
    def from_grid(grid: SudokuGrid) -> State:
        """
        Creates an initial state for a given grid.

        Parameters:
        -----------
        grid: SudokuGrid
            an initial state of the sudoku grid

        Return:
        --------
        state: State
            a state matching the grid
        """
        # TODO:
        # Create an initial state as stated in the docstring
        #
        # tips.
        # - to enumerate over the grid use:
        #   `for (row, col), val in grid.enumerate():`
        raise NotImplementedError("not implemented — remove this line")


class FirstFailSudokuSolver(SudokuSolver):
    """
    A first-fail backtracking sudoku solver.
    It first tries to fill cells with smallest number of available values.
    """

    state: State

    def __init__(self, puzzle, time_limit):
        super().__init__(puzzle, time_limit)
        self.state = State.from_grid(puzzle)

    def run_algorithm(self) -> SudokuGrid | None:
        with recursion_limit_set_to(self._puzzle.size**3):
            if self._dfs():
                return self.state.grid
            return None

    def _dfs(self) -> bool:
        """
        Performs a first-fail depth-first-search to solve the sudoku puzzle.
        It always chooses a variable with the smallest domain and tries it first.

        Return:
        --------
        solved: bool
            `True` - if method found the solution
            `False` - otherwise
        """

        a = self._choose_variable()
        if a is None:
            return True

        var, domain = a
        self.state.assign(var, domain.pop())
        if not self._dfs():
            self.state.remove_assignment(var)
            return False
        return True
        # TODO:
        # Implement the search.
        # 1. choose a free variable using `self._choose_variable`
        #   - if there is None, the solver has succeeded
        # 2. if there is a timeout, raise an appropriate exception
        # 3. try to assign a value to the variable and run the method recursively
        #   - take a value from the variable's domain
        #   - use self.state.assign to assign a value
        #   - use self.state.remove_assignment to revert the assignment
        # 4. return `False` if the solution has not been found

    def _choose_variable(self) -> tuple[Variable, Domain] | None:
        """
        Finds a free variable with the smallest domain.

        Return:
        --------
        var_dom: tuple[Variable, Domain] | None:
            if there are no free variables left,returns `None`
            otherwise returns a variable with the smallest domain (together with its domain)
        """

        free_variables = self.state.free_variables
        if not free_variables:
            return None

        lowest_domain = float('inf'), None, None
        for var in free_variables:
            domain = self.state.domain(var)
            if len(domain) < lowest_domain[0]:
                lowest_domain = len(domain), domain, var

        return lowest_domain[1], lowest_domain[2]

        # TODO:
        # Implement the method according to the docstring.
        # Useful stuff:
        # - self.state.free_variables
        # - self.state.domain
        # - https://docs.python.org/3/library/functions.html#min
