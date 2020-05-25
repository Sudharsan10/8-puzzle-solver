# ---------------------------------------------------------------------------------------------------------------------- #
# Project   :-> 8 Tile Puzzle Solver
# Authors   :-> Sudharsan
# E-mail    :-> sudharsansci@gmail.com


# ---------------------------------------------------------------------------------------------------------------------- #
# Import Section for Importing library
# ---------------------------------------------------------------------------------------------------------------------- #
import unittest
import argparse
import numpy as np

import Python.TilePuzzleSolver.Solver.tile_puzzle_solver as tp


# ---------------------------------------------------------------------------------------------------------------------- #
# Class for the Solver Algorithm
# ---------------------------------------------------------------------------------------------------------------------- #
class TestTilePuzzleSolver(unittest.TestCase):
    def setUp(self) -> None:
        initial_state = np.array([1, 2, 3, 4, 5, 6, 7, 8, 0])
        final_state = np.array([1, 0, 2, 8, 5, 3, 4, 7, 6])
        self.solver = tp.TilePuzzleSolver(initial_state, final_state)

    def test_isSolvable(self):
        self.assertEqual(self.solver.isSolvable([1, 2, 3, 4, 5, 6, 7, 8, 0], [1, 2, 3, 4, 5, 6, 7, 8, 0]),
                         True, 'TilePuzzleSolver.isSolvable() func is broken')

    def test_generateUniqueNumber(self):
        self.assertEqual(self.solver.generateUniqueNumber(np.array([1, 2, 3, 4, 5, 6, 7, 8, 0])), 123456780,
                         'TilePuzzleSolver.generateUniqueNumber() is broken')

    def test_autoSolve(self):
        initial_state = np.array([1, 2, 3, 4, 5, 6, 7, 8, 0])
        final_state = np.array([1, 0, 2, 8, 5, 3, 4, 7, 6])
        obj1 = tp.TilePuzzleSolver(initial_state, final_state)
        sol1 = obj1.autoSolve()
        self.assertEqual(type(sol1[0]), type(initial_state), "TilePuzzleSolver.autoSolve() function is broken")

        final_state = np.array([1, 2, 3, 5, 4, 6, 7, 8, 0])
        obj2 = tp.TilePuzzleSolver(initial_state, final_state)
        sol2 = obj2.autoSolve()
        self.assertEqual(sol2[0], "Not Solvable!", "TilePuzzleSolver.autoSolve() function is broken")


# ---------------------------------------------------------------------------------------------------------------------- #


if __name__ == '__main__':
    unittest.main()
