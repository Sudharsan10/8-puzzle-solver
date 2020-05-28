"""
# ---------------------------------------------------------------------------------------------------------------------- #
# Project   :-> 8 Tile Puzzle solver
# Authors   :-> Sudharsan
# E-mail    :-> sudharsansci@gmail.com
# ---------------------------------------------------------------------------------------------------------------------- #
"""
# ---------------------------------------------------------------------------------------------------------------------- #
# Import Section for Importing library
# ---------------------------------------------------------------------------------------------------------------------- #
from ui.gui import *
from solver.tile_puzzle_solver import *


# ---------------------------------------------------------------------------------------------------------------------- #
# Class for the GUI Controller
# ---------------------------------------------------------------------------------------------------------------------- #
class GUIController:
    """
    GUIController class handles the data from solver to UI and vice versa
    """
    def __init__(self):
        # Flags for layout and toggle hide or view methods
        self.solver = None
        self.data_controller = []
        # ---> GUI creation <--- #
        self.app = QtWidgets.QApplication(sys.argv)
        self.main_window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow(self, self.main_window)
        self.ui.setupUi()

    # ---> App Control <--- #
    def start_GUI(self):
        """
        Starts the UI app and show them
        Returns: None
        """
        # PyQt UI Object creation and visualisation
        self.main_window.show()
        sys.exit(self.app.exec_())
        pass

    def close_GUI(self):
        """
        Does Nothing as of now
        Returns: None
        """
        # destroy/close PyQt UI Object created ands exit
        pass

    def autoSolve(self, data: UIData) -> None:
        """
        AutoSolve function check for solution feasibility and get a solution
        Args:
            data: UIData
                data from ui to solver

        Returns: None

        """
        if self.IsSolvable(data):
            self.solver = TilePuzzleSolver(np.array(data.init), np.array(data.goal))
            self.solver.bruteForceExplorationBFS()
            path = self.solver.backTrack(self.solver.goal_id)
            self.ui.printSolution(path)
        else:
            self.ui.printWindow.setText("The given input is NOT solvable! \n Try different input value")

    def IsSolvable(self, data: UIData) -> bool:
        """
        Checks for solution feasibility
        Args:
            data: UIData
                data from ui to solver

        Returns:

        """
        if TilePuzzleSolver.isSolvable(data.init, data.goal):
            self.ui.printWindow.setText("Yes, the given input is solvable")
            return True
        else:
            self.ui.printWindow.setText("The given input is NOT solvable!")
            return False


if __name__ == '__main__':
    gui = GUIController()
    gui.start_GUI()
