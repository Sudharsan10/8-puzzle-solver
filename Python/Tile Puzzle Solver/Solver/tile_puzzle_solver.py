# ---------------------------------------------------------------------------------------------------------------------- #
# Project   :-> Eight Tile Puzzle Solver
# Authors   :-> Sudharsan
# E-mail    :-> sudharsansci@gmail.com

# ---------------------------------------------------------------------------------------------------------------------- #
# Import Section for Importing library
# ---------------------------------------------------------------------------------------------------------------------- #
import os, sys, random, math, argparse, time
import numpy as np

# ---------------------------------------------------------------------------------------------------------------------- #
# Class for the Solver Algorithm
# ---------------------------------------------------------------------------------------------------------------------- #
# ---------------------------------------------------------------------------------------------------------------------- #


class TilePuzzleSolver:
    def __init__(self, init_state: list, goal_state: list) -> None:
        pass

    def breadthFirstAlgorithm(self) -> int:
        pass

    def findNeighbors(self) -> None:
        pass

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

        pass

    def solution(self) -> None:
        pass
