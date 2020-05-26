# ---------------------------------------------------------------------------------------------------------------------- #
# Project   :-> 8 Tile Puzzle solver
# Authors   :-> Sudharsan
# E-mail    :-> sudharsansci@gmail.com

# ---------------------------------------------------------------------------------------------------------------------- #
# Import Section for Importing library
# ---------------------------------------------------------------------------------------------------------------------- #
from Python.TilePuzzleSolver.ui.gui import *
from Python.TilePuzzleSolver.solver.tile_puzzle_solver import *


# ---------------------------------------------------------------------------------------------------------------------- #
# Class for the GUI Controller
# ---------------------------------------------------------------------------------------------------------------------- #
class GUIController:
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
    def startGUI(self):
        # PyQt UI Object creation and visualisation
        self.main_window.show()
        sys.exit(self.app.exec_())
        pass

    def closeGUI(self):
        # destroy/close PyQt UI Object created ands exit
        pass

    def autoSolve(self, data: UIData) -> None:
        if self.IsSolvable(data):
            self.solver = TilePuzzleSolver(np.array(data.init), np.array(data.goal))
            self.solver.bruteForceExplorationBFS()
            path = self.solver.backTrack(self.solver.goal_id)
            self.ui.enableSim(path)
        else:
            self.ui.printWindow.setText("The given input is NOT solvable! \n Try different input value")

    def IsSolvable(self, data: UIData) -> bool:
        if TilePuzzleSolver.isSolvable(data.init, data.goal):
            self.ui.printWindow.setText("Yes, the given input is solvable")
            return True
        else:
            self.ui.printWindow.setText("The given input is NOT solvable!")
            return False


if __name__ == '__main__':
    gui = GUIController()
    gui.startGUI()
