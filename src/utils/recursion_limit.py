import sys


class recursion_limit_set_to:
    """
    A context manager temporarily overriding the recursion limit.
    For more details read: https://note.nkmk.me/en/python-sys-recursionlimit/

    Attributes:
    -----------
    original_limit: int
        the recursion limit before the override
    limit: int
        a desired recursion limit
    """

    original_limit: int
    limit: int

    def __init__(self, limit: int) -> None:
        """
        Initialize the context manager.

        Parameters:
        -----------
        limit: int
            a desired recursion limit
        """

        # TODO:
        # 1. set the `limit` attribute using the parameter
        # 2. set the `original_limit` attribute using a correct function form `sys` module
        #
        # tip. read class documentation
        raise NotImplementedError("not implemented — remove this line")

    def __enter__(self, *args, **kwargs) -> None:
        # TODO:
        # Override the recursion limit according to the class documentation
        raise NotImplementedError("not implemented — remove this line")

    def __exit__(self, *args) -> bool:
        # TODO:
        # Restore the original recursion limit according to the class documentation
        raise NotImplementedError("not implemented — remove this line")
