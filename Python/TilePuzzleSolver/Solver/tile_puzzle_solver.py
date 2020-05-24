# ---------------------------------------------------------------------------------------------------------------------- #
# Project   :-> 8 Tile Puzzle Solver
# Authors   :-> Sudharsan
# E-mail    :-> sudharsansci@gmail.com

# ---------------------------------------------------------------------------------------------------------------------- #
# Import Section for Importing library
# ---------------------------------------------------------------------------------------------------------------------- #
import os, sys, random, math, argparse, time, numpy as np
from queue import Queue


# ---------------------------------------------------------------------------------------------------------------------- #
# Class for the Solver Algorithm
# ---------------------------------------------------------------------------------------------------------------------- #
class Node:
    """
    Custom made data structure using class to store the node info.
    """

    def __init__(self, unique_number: int, state: np.array, index: int = None, parent: int = None,
                 hist: int = None) -> None:
        """

        Args:
            state: np.array
                Current State of the node
            index: int
                Index of the blank tile
            parent: int
                current state's parent id
            hist: int
                Current state's parent state's blank_tile_index
        """
        self.id = unique_number
        self.current_state = state
        self.blank_tile_index = index
        self.parent_id = parent
        self.hist_blank_tile_index = {hist}

