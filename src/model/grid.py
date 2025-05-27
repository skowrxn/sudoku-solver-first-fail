from __future__ import annotations
from dataclasses import dataclass
import math  # noqa
import numpy as np
import numpy.typing as npt


@dataclass(frozen=True, slots=True)
class SudokuGrid:
    """
    Represents a sudoku puzzle grid, i.e.,
    a square `n`x`n` grid split into `n` equal square blocks.
    An example below is of size 9x9 and has 9 blocks:

    ```
    -------------------------
    | 4,5,3 | 7,8,6 | 9,2,1 |
    | 1,2,9 | 4,5,3 | 6,8,7 |
    | 7,8,6 | 1,2,9 | 3,5,4 |
    -------------------------
    | 5,6,4 | 8,9,7 | 1,3,2 |
    | 2,3,1 | 5,6,4 | 7,9,8 |
    | 8,9,7 | 2,3,1 | 4,6,5 |
    -------------------------
    | 3,4,2 | 6,7,5 | 8,1,9 |
    | 9,1,8 | 3,4,2 | 5,7,6 |
    | 6,7,5 | 9,1,8 | 2,4,3 |
    -------------------------
    ```

    The blocks are indexed left to right, top to bottom, e.g.:

    ```
    -------------------------
    |       |       |       |
    |   0   |   1   |   2   |
    |       |       |       |
    -------------------------
    |       |       |       |
    |   3   |   4   |   5   |
    |       |       |       |
    -------------------------
    |       |       |       |
    |   6   |   7   |   8   |
    |       |       |       |
    -------------------------
    ```

    The grid itself follows the numpy indexing,
    - first index is the row number (`y`-coordinate)
    - second index is the column number (`x`-coordinate).
    Given `n`x`n` grid, the indexing looks as follows:

    ```
     (0,0) ------ (0,n-1)
       |             |
       |             |
       |             |
    (n-1,0) ---- (n-1,n-1)
    ```

    Protected Attributes:
    ---------------------
    _array: npt.NDArray[np.uint]
        Underlying representation of the grid.
        Uses dtype=np.uint to ensure its values are non-negative integer numbers.

    Properties:
    -----------
    size: int
        size of the grid
    block_size: int
        size of the single block

    Methods:
    --------
    __getitem__(coords: tuple[int, int]) -> np.uint:
        returns a value at the given coordinates
    __setitem__(coords: tuple[int,int], value: int) -> None:
        puts a value in the given cell of the grid
    enumerate() -> np.ndenumerate
        enumerates over the grid cells
    block_index(cell_row: int, cell_column: int) -> int:
        returns block index of the given cell
    block(block_index: int) -> npt.NDArray[np.uint]
        returns a block of the grid with the given index
    copy() -> SudokuGrid:
        returns a copy of the grid

    Static Methods:
    ---------------
    from_text(lines: list[str]) -> SudokuGrid:
        creates the grid from a textual representation
    """

    _array: npt.NDArray[np.uint]

    def __post_init__(self) -> None:
        rows, columns = self._array.shape
        if self._array.ndim != 2 or rows != columns or not math.sqrt(rows).is_integer():
            raise ValueError

    @property
    def size(self) -> int:
        """
        Returns size of the grid.

        Return:
        --------
        size: int
            the size of the grid, e.g. 9 for a 9x9 grid.
        """
        return self._array.shape[0]

    @property
    def block_size(self) -> int:
        """
        Returns size of a single block.

        Return:
        --------
        size: int
            the size of a single block, e.g. 3 for a 9x9 grid.
        """
        return int(math.sqrt(self._array.shape[0]))

    def __getitem__(self, coords: tuple[int, int]) -> np.uint:
        """
        Returns a value of the given cell in the grid.

        Parameters:
        -----------
        coords: tuple[int, int]
            coordinates (row, col) of the cell
        Return:
        --------
        value: np.uint
            a numpy array with values from the specified block
        """
        return self._array[coords]

    def __setitem__(self, coords: tuple[int, int], value: int) -> None:
        """
        Puts a value in the given cell of the grid.

        Parameters:
        -----------
        coords: tuple[int, int]
            coordinates (row, col) of the cell
        value: int
            value to be stored in the cell
        """
        self._array[coords] = value

    def enumerate(self) -> np.ndenumerate:
        """
        Returns an enumerator over the grid elements.
        See: https://numpy.org/doc/2.2/reference/generated/numpy.ndenumerate.html

        Return:
        --------
        enumerate: np.ndenumerate
            an enumerator over the grid
        """
        return np.ndenumerate(self._array)
    
    def flatten(self) -> npt.NDArray[np.uint]:
        """
        Returns a 1D copy of the grid array.
        See: https://numpy.org/doc/2.2/reference/generated/numpy.ndarray.flatten.html

        Return:
        --------
        flat_grid: npt.NDArray[np.uint]
            a flat copy of the array
        """
        return self._array.flatten()

    def block_index(self, cell_row: int, cell_column: int) -> int:
        """
        Returns a block index for a given cell.

        Parameters:
        -----------
        cell_row: int
            index of the cell row
        cell_column: int
            index of the cell column

        Return:
        --------
        block_index: int
            index of the block the specified cell belongs to
        """

        a = cell_column // self.block_size
        b = cell_row // self.block_size
        b *= self.block_size
        return a+b

    def block(self, block_index: int) -> npt.NDArray[np.uint]:
        """
        Returns a single block with a given index.

        Parameters:
        -----------
        block_index: int
            index of the block

        Return:
        --------
        block: npt.NDArray[np.uint]
            a numpy array with values from the specified block
        """
        # TODO:
        # - implement the method according to the docstring
        # tip 1. use array slicing: https://www.w3schools.com/python/numpy/numpy_array_slicing.asp
        # tip 2. check the docstring of the class to know what is the block index
        raise NotImplementedError("not implemented — copy from the previous lab")

    def copy(self) -> SudokuGrid:
        """
        Creates copy of the grid.

        Return:
        -------
        copy: SudokuGrid
            a copy of the current grid
        """
        return SudokuGrid(self._array.copy())

    def __str__(self) -> str:
        """
        Prints the grid in a pretty format, e.g.

        ```
        -------------------------
        | 4,5,3 | 7,8,6 | 9,2,1 |
        | 1,2,9 | 4,5,3 | 6,8,7 |
        | 7,8,6 | 1,2,9 | 3,5,4 |
        -------------------------
        | 5,6,4 | 8,9,7 | 1,3,2 |
        | 2,3,1 | 5,6,4 | 7,9,8 |
        | 8,9,7 | 2,3,1 | 4,6,5 |
        -------------------------
        | 3,4,2 | 6,7,5 | 8,1,9 |
        | 9,1,8 | 3,4,2 | 5,7,6 |
        | 6,7,5 | 9,1,8 | 2,4,3 |
        -------------------------
        ```

        Return:
        --------
        ascii_representation: str
            string containing a pretty ascii representation of the grid
        """
        # TODO:
        # Implement the method according to the docstring.
        # - if `lines` are ill-formatted, raise a ValueError
        # tip. there are many ways to initialize an array
        #      the easiest is to start with normal lists:
        #      https://numpy.org/devdocs/user/basics.creation.html#converting-python-sequences-to-numpy-arrays
        raise NotImplementedError("not implemented — copy from the previous lab")

    @staticmethod
    def from_text(lines: list[str]) -> SudokuGrid:
        """
        Reads a grid from basic textual representation, e.g.

        ```
        4,5,0,7,8,0,9,0,0
        0,2,0,4,0,3,6,0,0
        0,8,6,1,2,0,0,0,0
        0,6,0,0,9,7,1,3,0
        2,3,0,5,0,4,0,0,8
        0,0,7,2,0,1,4,0,0
        3,0,2,0,7,0,0,0,9
        9,0,8,0,0,0,0,0,6
        0,7,5,0,0,0,2,4,0
        ```

        Parameters:
        -----------
        lines: list[str]
            lines containing the textual representation

        Return:
        ---------
        grid: SudokuGrid
            a new sudoku grid
        """

        # TODO:
        # Implement the method according to the docstring.
        # - if `lines` are ill-formatted, raise a ValueError
        # tip. there are many ways to initialize an array
        #      the easiest is to start with normal lists:
        #      https://numpy.org/devdocs/user/basics.creation.html#converting-python-sequences-to-numpy-arrays
        raise NotImplementedError("not implemented — copy from the previous lab")
