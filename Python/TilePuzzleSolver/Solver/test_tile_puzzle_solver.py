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
        self.solver = tp.TilePuzzleSolver(initial_state, initial_state)

    def test_isSolvable(self):
        self.assertEqual(self.solver.isSolvable([1, 2, 3, 4, 5, 6, 7, 8, 0], [1, 2, 3, 4, 5, 6, 7, 8, 0]),
                         True, 'isSolvable() func is broken')

    def test_generateUniqueNumber(self):
        self.assertEqual(self.solver.generateUniqueNumber(np.array([1, 2, 3, 4, 5, 6, 7, 8, 0])), 123456780,
                         'generateUniqueNumber() is broken')


# ---------------------------------------------------------------------------------------------------------------------- #


if __name__ == '__main__':
    unittest.main()
