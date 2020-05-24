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
    def isSolvable(initial_state: list, goal_state: list) -> bool:
        """
        isSolvable(initial_state, goal_state) -> bool

        It takes the initial state and goal state unique number and checks for solution feasibility.

        Args:
            initial_state: int
                A 9 digit integer
            goal_state: int
                A 9 digit integer

        Returns: bool
            Returns True if the solution is feasible for the given states else False.

        """

        # ---> Step 01: Copy the arg <--- #
        init, goal = initial_state.copy(), goal_state.copy()

        # ---> Step 02: Remove zero from the args <--- #
        init.remove(0)
        goal.remove(0)

        # ---> Step 03: Initialize flip counter <---#
        init_flip_count, goal_flip_count = 0, 0

        # initialize Miscellaneous variable
        n = len(init)

        for i in range(0, n):
            temp_i = init[i:]
            temp_g = goal[i:]
            for j in range(0, len(temp_i)):
                if temp_i[j] < init[i]:
                    init_flip_count += 1
                if temp_g[j] < goal[i]:
                    goal_flip_count += 1
        return init_flip_count % 2 == 0 and goal_flip_count % 2 == 0

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

    def findNeighbors(self, node: Node) -> None:
        """
        A Function to get the possible neighbor index based on blank tile location
        Returns: None

        """
        neighbors = self.neighbours[node.blank_tile_index].difference(node.hist_blank_tile_index)
        self.makeMove(neighbors, node)

    def bruteForceExplorationBFS(self) -> None:
        """
        This Function explores the possible states of the Tile Puzzle using breadth first search Algorithm
        Returns: None

        """
        while not self.que.empty() and not self.exit_flag:
            self.current_node = self.que.get()
            self.findNeighbors(self.current_node)

        if self.exit_flag:
            print("Goal Found")
        print(self.nodes.__len__())
