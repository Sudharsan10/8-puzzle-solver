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


class TilePuzzleSolver:
    def __init__(self, init_state: np.array, goal_state: np.array) -> None:
        """

        Args:
            args.init_state: np.array
                Its a 1D numpy array
            args.goal_state: np.array
                Its a 1D numpy array
        """
        # ---> Initialize variables <--- #
        self.init_state = init_state
        self.goal_state = goal_state
        self.neighbours = {0: {1, 3},
                           1: {0, 2, 4},
                           2: {1, 5},
                           3: {0, 4, 6},
                           4: {1, 3, 5, 7},
                           5: {2, 4, 8},
                           6: {3, 7},
                           7: {4, 6, 8},
                           8: {5, 7},
                           }
        self.nodes = dict()
        self.que = Queue()
        self.exit_flag = False
        self.init_id = self.generateUniqueNumber(init_state)
        self.goal_id = self.generateUniqueNumber(goal_state)

        # ---> Find the blank Tile Location <--- #
        blank_tile_index = np.argmin(self.init_state)

        # ---> Create a Node for init_state <--- #
        self.current_node = Node(self.init_id, self.init_state,
                                 int(blank_tile_index),
                                 self.init_id,
                                 int(blank_tile_index))

        # ---> Add Current node to the Nodes dictionary & queue <--- #
        self.nodes[self.current_node.id] = self.current_node
        self.que.put(self.current_node)

    @staticmethod
    def generateUniqueNumber(node: np.array, unique_seq: np.array = np.array([100000000, 10000000, 1000000, 100000, 10000, 1000, 100, 10, 1])) -> int:
        """
        Args:
            unique_seq: np.array
                np.array([100000000, 10000000, 1000000, 100000, 10000, 1000, 100, 10, 1]) the multiplier
            node: np.array
                Its a 1D array

        Returns: int
                A 9 digit int

        """
        return node @ unique_seq
