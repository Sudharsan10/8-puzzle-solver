# ---------------------------------------------------------------------------------------------------------------------- #
# Project   :-> 8 Tile Puzzle solver
# Authors   :-> Sudharsan
# E-mail    :-> sudharsansci@gmail.com

# ---------------------------------------------------------------------------------------------------------------------- #
# Import Section for Importing library
# ---------------------------------------------------------------------------------------------------------------------- #import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from Python.TilePuzzleSolver.ui.gui import *


# ---------------------------------------------------------------------------------------------------------------------- #
# Class for the GUI Controller
# ---------------------------------------------------------------------------------------------------------------------- #
class GUIController:
    def __init__(self):
        # Flags for layout and toggle hide or view methods
        self.data_controller = []

        # ---> GUI creation <--- #
        self.app = QtWidgets.QApplication(sys.argv)
        self.main_window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow(self)
        self.ui.setupUi(self.main_window)

        pass

    # ---> App Control <--- #
    def startGUI(self):
        # PyQt UI Object creation and visualisation
        self.main_window.show()
        sys.exit(self.app.exec_())
        pass

    def closeGUI(self):
        # destroy/close PyQt UI Object created ands exit
        pass

    # ---> Program Control <--- #
    def autoSolve(self):
        pass

    def IsSolvable(self):
        pass

    def simulate(self):
        pass

    def reset(self):
        # self.layout.reset()
        pass

    # ---> Simulation Controls <--- #
    def playSim(self):
        pass

    def pauseSim(self):
        pass

    def resetSim(self):
        pass

    def toggleManualControl(self):
        pass

    def previousState(self):
        pass

    def nextState(self):
        pass


if __name__ == '__main__':
    gui = GUIController()
    gui.startGUI()
