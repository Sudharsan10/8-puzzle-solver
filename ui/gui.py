# ---------------------------------------------------------------------------------------------------------------------- #
# Project   :-> 8 Tile Puzzle solver
# Authors   :-> Sudharsan
# E-mail    :-> sudharsansci@gmail.com

# ---------------------------------------------------------------------------------------------------------------------- #
# Import Section for Importing library
# ---------------------------------------------------------------------------------------------------------------------- #
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QFile
from PyQt5.QtGui import QIntValidator, QCursor, QIcon
from data.ui_data import *
from ui.css_styles import *
import sys


# ---------------------------------------------------------------------------------------------------------------------- #
# Class for the GUI
# ---------------------------------------------------------------------------------------------------------------------- #
class Ui_MainWindow(object):
    def __init__(self, controller: object, main_window: QtWidgets):
        """
        Initialize the controller, UI objects and UI widget attributes
        Args:
            controller: gui_controller object
                Controller object to control the app flow
            main_window: QtWidgets object
                UI Object
        """
        # ---> Attributes <--- #
        self.data = UIData()
        self.data.solution = []
        self.counter = 0
        self.is_solvable_flag = False
        self.main_window = main_window
        self.centralwidget = QtWidgets.QWidget(self.main_window)
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.container = QtWidgets.QWidget(self.centralwidget)
        self.container_grid = QtWidgets.QGridLayout(self.container)

        self.initial_state = QtWidgets.QWidget(self.container)
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.initial_state)
        self.init = QtWidgets.QWidget(self.initial_state)
        self.init_input_grid = QtWidgets.QGridLayout(self.init)
        self.initLabel = QtWidgets.QLabel(self.init)
        self.i0 = QtWidgets.QLineEdit(self.init)
        self.i1 = QtWidgets.QLineEdit(self.init)
        self.i2 = QtWidgets.QLineEdit(self.init)
        self.i3 = QtWidgets.QLineEdit(self.init)
        self.i4 = QtWidgets.QLineEdit(self.init)
        self.i5 = QtWidgets.QLineEdit(self.init)
        self.i6 = QtWidgets.QLineEdit(self.init)
        self.i7 = QtWidgets.QLineEdit(self.init)
        self.i8 = QtWidgets.QLineEdit(self.init)

        self.goal_state = QtWidgets.QWidget(self.container)
        self.gridLayout_5 = QtWidgets.QGridLayout(self.goal_state)
        self.goal = QtWidgets.QWidget(self.goal_state)
        self.goal_input_grid = QtWidgets.QGridLayout(self.goal)
        self.g0 = QtWidgets.QLineEdit(self.goal)
        self.g1 = QtWidgets.QLineEdit(self.goal)
        self.g2 = QtWidgets.QLineEdit(self.goal)
        self.g3 = QtWidgets.QLineEdit(self.goal)
        self.g4 = QtWidgets.QLineEdit(self.goal)
        self.g5 = QtWidgets.QLineEdit(self.goal)
        self.g6 = QtWidgets.QLineEdit(self.goal)
        self.g7 = QtWidgets.QLineEdit(self.goal)
        self.g8 = QtWidgets.QLineEdit(self.goal)
        self.goalLabel = QtWidgets.QLabel(self.goal)

        self.sim = QtWidgets.QWidget(self.container)
        self.simulation_grid = QtWidgets.QGridLayout(self.sim)
        self.controls = QtWidgets.QWidget(self.sim)
        self.sim_controls_grid = QtWidgets.QGridLayout(self.controls)
        self.toggleManualButton = QtWidgets.QPushButton(self.controls)
        self.nextButton = QtWidgets.QPushButton(self.controls)
        self.previousButton = QtWidgets.QPushButton(self.controls)
        self.pauseButton = QtWidgets.QPushButton(self.controls)
        self.resetButton = QtWidgets.QPushButton(self.controls)
        self.startButton = QtWidgets.QPushButton(self.controls)
        self.output = QtWidgets.QWidget(self.sim)
        self.sim_output_text_grid = QtWidgets.QGridLayout(self.output)

        self.out0 = QtWidgets.QLabel(self.output)
        self.out1 = QtWidgets.QLabel(self.output)
        self.out2 = QtWidgets.QLabel(self.output)
        self.out3 = QtWidgets.QLabel(self.output)
        self.out4 = QtWidgets.QLabel(self.output)
        self.out5 = QtWidgets.QLabel(self.output)
        self.out6 = QtWidgets.QLabel(self.output)
        self.out7 = QtWidgets.QLabel(self.output)
        self.out8 = QtWidgets.QLabel(self.output)

        self.sim_controls_label = QtWidgets.QLabel(self.sim)
        self.solution = QtWidgets.QWidget(self.container)
        self.verticalLayout = QtWidgets.QVBoxLayout(self.solution)
        self.output_window_label = QtWidgets.QLabel(self.solution)
        self.printWindow = QtWidgets.QTextBrowser(self.solution)
        self.control = QtWidgets.QWidget(self.container)
        self.action_button_layout = QtWidgets.QGridLayout(self.control)
        self.options = QtWidgets.QLabel(self.control)
        self.findSolutionButton = QtWidgets.QPushButton(self.control)
        self.isSolvableButton = QtWidgets.QPushButton(self.control)
        self.appResetButton = QtWidgets.QPushButton(self.control)
        self.simulationButton = QtWidgets.QPushButton(self.control)
        self.menubar = QtWidgets.QMenuBar(self.main_window)
        self.settings = QtWidgets.QMenu(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self.main_window)
        self.actionSave = QtWidgets.QAction(self.main_window)
        self.actionCopy = QtWidgets.QAction(self.main_window)

        self.controller = controller
        self.IntValidator = QIntValidator(0, 9)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.nextState)

        self.resetALl()

    def validateInputData(self) -> bool:
        """
        Validate the input data -Init_state and goal_state, for int.
        Returns: bool
            Returns True if the input data passes validation test, else False.

        """
        self.data.init = []
        self.data.goal = []
        init_raw = [self.i0.text(), self.i1.text(), self.i2.text(),
                    self.i3.text(), self.i4.text(), self.i5.text(),
                    self.i6.text(), self.i7.text(), self.i8.text()]
        goal_raw = [self.g0.text(), self.g1.text(), self.g2.text(),
                    self.g3.text(), self.g4.text(), self.g5.text(),
                    self.g6.text(), self.g7.text(), self.g8.text()]

        for x, y in zip(init_raw, goal_raw):
            if self.IntValidator.validate(x, 0)[0] != 2 or self.IntValidator.validate(y, 0)[0] != 2:
                self.printWindow.setText("Bad Input! Please Enter only numbers from 0-9!")
                return False
            self.data.init.append(int(x))
            self.data.goal.append(int(y))

        return True

    def updateSimOut(self, data: list) -> None:
        """
        A function to update the solution Simulation Area
        Args:
            data: list
                list of int data
        Returns: None
        """
        self.out0.setText(str(data[0]))
        self.out1.setText(str(data[1]))
        self.out2.setText(str(data[2]))
        self.out3.setText(str(data[3]))
        self.out4.setText(str(data[4]))
        self.out5.setText(str(data[5]))
        self.out6.setText(str(data[6]))
        self.out7.setText(str(data[7]))
        self.out8.setText(str(data[8]))

    def clearSimOut(self) -> None:
        """
        A function to reset the simulation widget and reset to init_State
        Returns: None
        """
        self.out0.clear()
        self.out1.clear()
        self.out2.clear()
        self.out3.clear()
        self.out4.clear()
        self.out5.clear()
        self.out6.clear()
        self.out7.clear()
        self.out8.clear()
        self.counter = 0
        self.timer.stop()
        if self.data.solution:
            self.updateSimOut(self.data.solution[0])
            if not self.startButton.isVisible():
                self.nextButton.setVisible(True)

    def isSolvable(self) -> None:
        """
        Upon triggered by IsSolvable Button click, Checks for valid input data and then checks for solution feasibility.
        Returns: None
        """
        if self.validateInputData():
            self.is_solvable_flag = self.controller.IsSolvable(self.data)

    def printSolution(self, solution: list) -> None:
        """
        Prints the Solution in the Solution window.
        Args:
            solution: list
                Solution to the puzzle
        Returns: None
        """
        out = ""
        self.simulationButton.setVisible(True)
        self.data.solution = solution
        for x in solution:
            out = out + ''.join(ch for ch in str(x.reshape(3, 3)) if ch not in {'[', ']'}) + '\n\n'
        self.printWindow.setText(out)

    def simulation(self) -> None:
        """
        Upon successful search, this function is called to Enables the simulation controls
        Returns: None
        """
        self.pauseButton.setVisible(True)
        self.startButton.setVisible(True)
        self.resetButton.setVisible(True)
        self.toggleManualButton.setVisible(True)
        self.updateSimOut(self.data.solution[0])

    def findSolution(self) -> None:
        """
        Upon triggered by find Solution button, it checks for input data validations and calls auto solve function.
        Returns: None
        """
        if self.validateInputData():
            self.controller.autoSolve(self.data)

    def resetALl(self) -> None:
        """
        Resets the program's input, output and simulation area.
        Returns: None
        """
        self.data.solution = []
        self.i0.clear()
        self.i1.clear()
        self.i2.clear()
        self.i3.clear()
        self.i4.clear()
        self.i5.clear()
        self.i6.clear()
        self.i7.clear()
        self.i8.clear()
        self.g0.clear()
        self.g1.clear()
        self.g2.clear()
        self.g3.clear()
        self.g4.clear()
        self.g5.clear()
        self.g6.clear()
        self.g7.clear()
        self.g8.clear()
        self.clearSimOut()
        self.simulationButton.setVisible(False)
        self.pauseButton.setVisible(False)
        self.previousButton.setVisible(False)
        self.startButton.setVisible(False)
        self.resetButton.setVisible(False)
        self.nextButton.setVisible(False)
        self.toggleManualButton.setVisible(False)
        self.printWindow.setText("Program has been Reset!!")

    def toggleManual(self) -> None:
        """
        Toggle the manual control and automated solution sim.
        Returns: None
        """
        if self.nextButton.isVisible():
            self.startButton.setVisible(True)
            self.pauseButton.setVisible(True)
            self.nextButton.setVisible(False)
            self.previousButton.setVisible(False)
            self.clearSimOut()
            self.updateSimOut(self.data.solution[0])
        else:
            self.startButton.setVisible(False)
            self.pauseButton.setVisible(False)
            self.nextButton.setVisible(True)
            self.previousButton.setVisible(True)
            self.updateSimOut(self.data.solution[0])

    def startSim(self) -> None:
        """
        start the solution simulation
        Returns: None
        """
        self.timer.start(1000)  # every 10,000 millisecond

    def pauseSim(self) -> None:
        """
        Pauses the simulation until start is pressed again
        Returns: None
        """
        self.timer.stop()

    def nextState(self) -> None:
        """
        Updates the next solution state of the solution
        Returns: None
        """
        self.counter += 1
        if self.counter < self.data.solution.__len__():
            if not self.startButton.isVisible():
                self.previousButton.setVisible(True)
            self.updateSimOut(self.data.solution[self.counter])
        if self.counter == self.data.solution.__len__() - 1:
            self.nextButton.setVisible(False)

    def previousState(self) -> None:
        """
        Updates to previous solution state of the solution
        Returns: None
        """
        self.counter -= 1
        if self.counter >= 0:
            if not self.startButton.isVisible():
                self.nextButton.setVisible(True)
            self.updateSimOut(self.data.solution[self.counter])
        if self.counter == 0:
            self.previousButton.setVisible(False)

    def setupUi(self) -> None:
        """
        Initializes and sets up the GUI layout and widgets
        Returns: None
        """
        # ---> Main Window Initialization<--- #
        self.main_window.setObjectName("MainWindow")
        self.main_window.resize(829, 744)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_window.sizePolicy().hasHeightForWidth())
        self.main_window.setSizePolicy(sizePolicy)
        self.main_window.setMinimumSize(QtCore.QSize(700, 700))
        self.main_window.setAnimated(True)


        # ---> Central Widget Initialization<--- #
        self.centralwidget.setStyleSheet(css_centralWidget)
        self.centralwidget.setObjectName("centralwidget")

        # ---> Central Widget's Grid layout Initialization<--- #
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")

        # ---> Container Initialization<--- #
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.container.sizePolicy().hasHeightForWidth())

        self.container.setSizePolicy(sizePolicy)
        self.container.setMaximumSize(QtCore.QSize(700, 700))
        self.container.setStyleSheet("")
        self.container.setObjectName("container")

        # ---> Container's Grid layout Initialization<--- #
        self.container_grid.setContentsMargins(0, 0, 0, 0)
        self.container_grid.setSpacing(5)
        self.container_grid.setObjectName("container_grid")

        self.inputWidgets()
        self.simulationWidget()
        self.simOutputArea()
        self.solutionSection()
        self.programControls()
        self.menuBarWidget()
        self.tabOrderFunc()

    def inputWidgets(self) -> None:
        """
        Initializes the data input layouts and widgets
        Returns: None
        """
        # ---> Initial Widget <--- #
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.initial_state.sizePolicy().hasHeightForWidth())
        self.initial_state.setSizePolicy(sizePolicy)
        self.initial_state.setStyleSheet(css_no_border)
        self.initial_state.setObjectName("initial_state")

        # ---> Initial Widget layout<--- #
        self.horizontalLayout.setObjectName("horizontalLayout")

        # ---> Init Input Widget<--- #
        self.init.setMinimumSize(QtCore.QSize(200, 200))
        self.init.setObjectName("init")

        # ---> Init Input Widget's Layout <--- #
        self.init_input_grid.setObjectName("init_input_grid")

        self.initLabel.setMinimumSize(QtCore.QSize(0, 20))
        self.initLabel.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily(css_fontStyle)
        font.setPointSize(10)
        self.initLabel.setFont(font)
        self.initLabel.setTextFormat(QtCore.Qt.AutoText)
        self.initLabel.setScaledContents(False)
        self.initLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.initLabel.setObjectName("initLabel")
        self.init_input_grid.addWidget(self.initLabel, 1, 0, 1, 3)

        # ---> Init Input 00 <--- #
        font = QtGui.QFont()
        font.setFamily(css_fontStyle)
        font.setPointSize(22)
        self.i0.setFont(font)
        self.i0.setStyleSheet(css_inputText)
        self.i0.setMaxLength(1)
        self.i0.setAlignment(QtCore.Qt.AlignCenter)
        self.i0.setObjectName("lineEdit")
        self.init_input_grid.addWidget(self.i0, 2, 0, 1, 1)

        # ---> Init Input 01 <--- #
        font = QtGui.QFont()
        font.setFamily(css_fontStyle)
        font.setPointSize(22)
        self.i1.setFont(font)
        self.i1.setAutoFillBackground(False)
        self.i1.setStyleSheet(css_inputText)
        self.i1.setMaxLength(1)
        self.i1.setAlignment(QtCore.Qt.AlignCenter)
        self.i1.setClearButtonEnabled(False)
        self.i1.setObjectName("i1")
        self.init_input_grid.addWidget(self.i1, 2, 1, 1, 1)

        # ---> Init Input 02 <--- #
        font = QtGui.QFont()
        font.setFamily(css_fontStyle)
        font.setPointSize(22)
        self.i2.setFont(font)
        self.i2.setAutoFillBackground(False)
        self.i2.setStyleSheet(css_inputText)
        self.i2.setMaxLength(1)
        self.i2.setAlignment(QtCore.Qt.AlignCenter)
        self.i2.setClearButtonEnabled(False)
        self.i2.setObjectName("i2")
        self.init_input_grid.addWidget(self.i2, 2, 2, 1, 1)

        # ---> Init Input 03 <--- #
        font = QtGui.QFont()
        font.setFamily(css_fontStyle)
        font.setPointSize(22)
        self.i3.setFont(font)
        self.i3.setAutoFillBackground(False)
        self.i3.setStyleSheet(css_inputText)
        self.i3.setMaxLength(1)
        self.i3.setAlignment(QtCore.Qt.AlignCenter)
        self.i3.setClearButtonEnabled(False)
        self.i3.setObjectName("i3")
        self.init_input_grid.addWidget(self.i3, 3, 0, 1, 1)

        # ---> Init Input 04 <--- #
        font = QtGui.QFont()
        font.setFamily(css_fontStyle)
        font.setPointSize(22)
        self.i4.setFont(font)
        self.i4.setAutoFillBackground(False)
        self.i4.setStyleSheet(css_inputText)
        self.i4.setMaxLength(1)
        self.i4.setAlignment(QtCore.Qt.AlignCenter)
        self.i4.setClearButtonEnabled(False)
        self.i4.setObjectName("i4")
        self.init_input_grid.addWidget(self.i4, 3, 1, 1, 1)

        # ---> Init Input 05 <--- #
        font = QtGui.QFont()
        font.setFamily(css_fontStyle)
        font.setPointSize(22)
        self.i5.setFont(font)
        self.i5.setAutoFillBackground(False)
        self.i5.setStyleSheet(css_inputText)
        self.i5.setMaxLength(1)
        self.i5.setAlignment(QtCore.Qt.AlignCenter)
        self.i5.setClearButtonEnabled(False)
        self.i5.setObjectName("i5")
        self.init_input_grid.addWidget(self.i5, 3, 2, 1, 1)

        # ---> Init Input 06 <--- #
        font = QtGui.QFont()
        font.setFamily(css_fontStyle)
        font.setPointSize(22)
        self.i6.setFont(font)
        self.i6.setAutoFillBackground(False)
        self.i6.setStyleSheet(css_inputText)
        self.i6.setMaxLength(1)
        self.i6.setAlignment(QtCore.Qt.AlignCenter)
        self.i6.setClearButtonEnabled(False)
        self.i6.setObjectName("i6")
        self.init_input_grid.addWidget(self.i6, 4, 0, 1, 1)

        # ---> Init Input 07 <--- #
        font = QtGui.QFont()
        font.setFamily(css_fontStyle)
        font.setPointSize(22)
        self.i7.setFont(font)
        self.i7.setAutoFillBackground(False)
        self.i7.setStyleSheet(css_inputText)
        self.i7.setMaxLength(1)
        self.i7.setAlignment(QtCore.Qt.AlignCenter)
        self.i7.setClearButtonEnabled(False)
        self.i7.setObjectName("i7")
        self.init_input_grid.addWidget(self.i7, 4, 1, 1, 1)

        # ---> Init Input 08 <--- #
        font = QtGui.QFont()
        font.setFamily(css_fontStyle)
        font.setPointSize(22)
        self.i8.setFont(font)
        self.i8.setAutoFillBackground(False)
        self.i8.setStyleSheet(css_inputText)
        self.i8.setMaxLength(1)
        self.i8.setAlignment(QtCore.Qt.AlignCenter)
        self.i8.setClearButtonEnabled(False)
        self.i8.setObjectName("i8")
        self.init_input_grid.addWidget(self.i8, 4, 2, 1, 1)

        self.horizontalLayout.addWidget(self.init)
        self.container_grid.addWidget(self.initial_state, 0, 0, 1, 1)

        # ---> Goal Input Widget <--- #
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.goal_state.sizePolicy().hasHeightForWidth())
        self.goal_state.setSizePolicy(sizePolicy)
        self.goal_state.setStyleSheet(css_no_border)
        self.goal_state.setObjectName("goal_state")

        # ---> Goal's grid <--- #
        self.gridLayout_5.setObjectName("gridLayout_5")

        # ---> Goal text grid Widget <--- #
        self.goal.setMinimumSize(QtCore.QSize(200, 200))
        self.goal.setObjectName("goal")

        # ---> Goal Input's grid <--- #
        self.goal_input_grid.setObjectName("goal_input_grid")

        # ---> Goal Input 00 <--- #
        font = QtGui.QFont()
        font.setFamily(css_fontStyle)
        font.setPointSize(22)
        self.g0.setFont(font)
        self.g0.setStyleSheet(css_inputText)
        self.g0.setMaxLength(1)
        self.g0.setAlignment(QtCore.Qt.AlignCenter)
        self.g0.setClearButtonEnabled(False)
        self.g0.setObjectName("g0")
        self.goal_input_grid.addWidget(self.g0, 2, 0, 1, 1)

        # ---> Goal Input 01 <--- #
        font = QtGui.QFont()
        font.setFamily(css_fontStyle)
        font.setPointSize(22)
        self.g1.setFont(font)
        self.g1.setStyleSheet(css_inputText)
        self.g1.setMaxLength(1)
        self.g1.setAlignment(QtCore.Qt.AlignCenter)
        self.g1.setClearButtonEnabled(False)
        self.g1.setObjectName("g1")
        self.goal_input_grid.addWidget(self.g1, 2, 1, 1, 1)

        # ---> Goal Input 02 <--- #
        font = QtGui.QFont()
        font.setFamily(css_fontStyle)
        font.setPointSize(22)
        self.g2.setFont(font)
        self.g2.setStyleSheet(css_inputText)
        self.g2.setMaxLength(1)
        self.g2.setAlignment(QtCore.Qt.AlignCenter)
        self.g2.setClearButtonEnabled(False)
        self.g2.setObjectName("g2")
        self.goal_input_grid.addWidget(self.g2, 2, 2, 1, 1)

        # ---> Goal Input 03 <--- #
        font = QtGui.QFont()
        font.setFamily(css_fontStyle)
        font.setPointSize(22)
        self.g3.setFont(font)
        self.g3.setStyleSheet(css_inputText)
        self.g3.setMaxLength(1)
        self.g3.setAlignment(QtCore.Qt.AlignCenter)
        self.g3.setClearButtonEnabled(False)
        self.g3.setObjectName("g3")
        self.goal_input_grid.addWidget(self.g3, 3, 0, 1, 1)

        # ---> Goal Input 04 <--- #
        font = QtGui.QFont()
        font.setFamily(css_fontStyle)
        font.setPointSize(22)
        self.g4.setFont(font)
        self.g4.setStyleSheet(css_inputText)
        self.g4.setMaxLength(1)
        self.g4.setAlignment(QtCore.Qt.AlignCenter)
        self.g4.setClearButtonEnabled(False)
        self.g4.setObjectName("g4")
        self.goal_input_grid.addWidget(self.g4, 3, 1, 1, 1)

        # ---> Goal Input 05 <--- #
        font = QtGui.QFont()
        font.setFamily(css_fontStyle)
        font.setPointSize(22)
        self.g5.setFont(font)
        self.g5.setStyleSheet(css_inputText)
        self.g5.setMaxLength(1)
        self.g5.setAlignment(QtCore.Qt.AlignCenter)
        self.g5.setClearButtonEnabled(False)
        self.g5.setObjectName("g5")
        self.goal_input_grid.addWidget(self.g5, 3, 2, 1, 1)

        # ---> Goal Input 06 <--- #
        font = QtGui.QFont()
        font.setFamily(css_fontStyle)
        font.setPointSize(22)
        self.g6.setFont(font)
        self.g6.setStyleSheet(css_inputText)
        self.g6.setMaxLength(1)
        self.g6.setAlignment(QtCore.Qt.AlignCenter)
        self.g6.setClearButtonEnabled(False)
        self.g6.setObjectName("g6")
        self.goal_input_grid.addWidget(self.g6, 4, 0, 1, 1)

        # ---> Goal Input 07 <--- #
        font = QtGui.QFont()
        font.setFamily(css_fontStyle)
        font.setPointSize(22)
        self.g7.setFont(font)
        self.g7.setStyleSheet(css_inputText)
        self.g7.setMaxLength(1)
        self.g7.setAlignment(QtCore.Qt.AlignCenter)
        self.g7.setClearButtonEnabled(False)
        self.g7.setObjectName("g7")
        self.goal_input_grid.addWidget(self.g7, 4, 1, 1, 1)

        # ---> Goal Input 08 <--- #
        font = QtGui.QFont()
        font.setFamily(css_fontStyle)
        font.setPointSize(22)
        self.g8.setFont(font)
        self.g8.setStyleSheet(css_inputText)
        self.g8.setMaxLength(1)
        self.g8.setAlignment(QtCore.Qt.AlignCenter)
        self.g8.setClearButtonEnabled(False)
        self.g8.setObjectName("g8")
        self.goal_input_grid.addWidget(self.g8, 4, 2, 1, 1)

        # ---> Goal Widget Label <--- #
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.goalLabel.sizePolicy().hasHeightForWidth())
        self.goalLabel.setSizePolicy(sizePolicy)
        self.goalLabel.setMinimumSize(QtCore.QSize(40, 20))
        self.goalLabel.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily(css_fontStyle)
        font.setPointSize(10)
        self.goalLabel.setFont(font)
        self.goalLabel.setScaledContents(False)
        self.goalLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.goalLabel.setObjectName("goalLabel")
        self.goal_input_grid.addWidget(self.goalLabel, 1, 0, 1, 3)

        self.gridLayout_5.addWidget(self.goal, 0, 0, 1, 1)
        self.container_grid.addWidget(self.goal_state, 0, 1, 1, 1)

    def simulationWidget(self) -> None:
        # ---> Simulation Widget <--- #
        self.sim.setAutoFillBackground(False)
        self.sim.setStyleSheet("border: none;")
        self.sim.setObjectName("sim")

        # ---> Simulation Widget's Grid <--- #
        self.simulation_grid.setObjectName("simulationt_grid")

        # ---> Simulation Widget's control Widget <--- #
        self.controls.setMinimumSize(QtCore.QSize(0, 137))
        self.controls.setObjectName("controls")

        # ---> Simulation control Widget's grid <--- #
        self.sim_controls_grid.setObjectName("sim_controls_grid")

        # ---> Sim control's toggle manual control button <--- #
        self.toggleManualButton.setMinimumSize(QtCore.QSize(0, 30))
        self.toggleManualButton.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(css_fontStyle)
        font.setPointSize(10)
        self.toggleManualButton.setFont(font)
        self.toggleManualButton.setStyleSheet(css_sim_ctrl_buttons)
        self.toggleManualButton.setAutoRepeat(False)
        self.toggleManualButton.setObjectName("toggleManualControl")
        self.sim_controls_grid.addWidget(self.toggleManualButton, 1, 1, 1, 3)

        # ---> Sim control's next state button <--- #
        self.nextButton.setMinimumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily(css_fontStyle)
        font.setPointSize(10)
        self.nextButton.setFont(font)
        self.nextButton.setStyleSheet(css_sim_ctrl_buttons)
        self.nextButton.setAutoRepeat(False)
        self.nextButton.setObjectName("nextButton")
        self.sim_controls_grid.addWidget(self.nextButton, 0, 4, 1, 1)

        # ---> Sim control's previous state button <--- #
        self.previousButton.setMinimumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily(css_fontStyle)
        font.setPointSize(10)
        self.previousButton.setFont(font)
        self.previousButton.setStyleSheet(css_sim_ctrl_buttons)
        self.previousButton.setAutoRepeat(False)
        self.previousButton.setObjectName("previousButton")
        self.sim_controls_grid.addWidget(self.previousButton, 0, 0, 1, 1)

        # ---> Sim control's pause button <--- #
        self.pauseButton.setMinimumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily(css_fontStyle)
        font.setPointSize(10)
        self.pauseButton.setFont(font)
        self.pauseButton.setStyleSheet(css_sim_ctrl_buttons)
        self.pauseButton.setAutoRepeat(False)
        self.pauseButton.setObjectName("pauseButton")
        self.sim_controls_grid.addWidget(self.pauseButton, 0, 1, 1, 1)

        # ---> Sim control's reset button <--- #
        self.resetButton.setMinimumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily(css_fontStyle)
        font.setPointSize(10)
        self.resetButton.setFont(font)
        self.resetButton.setStyleSheet(css_sim_ctrl_buttons)
        self.resetButton.setAutoRepeat(False)
        self.resetButton.setObjectName("resetButton")
        self.sim_controls_grid.addWidget(self.resetButton, 0, 3, 1, 1)

        # ---> Sim control's start button <--- #
        self.startButton.setMinimumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily(css_fontStyle)
        font.setPointSize(10)
        self.startButton.setFont(font)
        self.startButton.setStyleSheet(css_sim_ctrl_buttons)
        self.startButton.setAutoRepeat(False)
        self.startButton.setObjectName("startButton")
        self.sim_controls_grid.addWidget(self.startButton, 0, 2, 1, 1)

        self.simulation_grid.addWidget(self.controls, 1, 0, 1, 2)

    def simOutputArea(self) -> None:
        # ---> Simulation solution output widget <--- #
        self.output.setObjectName("output")

        # --->  Sim output text grid <--- #
        self.sim_output_text_grid.setHorizontalSpacing(5)
        self.sim_output_text_grid.setVerticalSpacing(30)
        self.sim_output_text_grid.setObjectName("sim_output_text_grid")

        # ---> Sim: Output 00 <--- #
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.out0.sizePolicy().hasHeightForWidth())
        self.out0.setSizePolicy(sizePolicy)
        self.out0.setMinimumSize(QtCore.QSize(50, 50))
        self.out0.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily(css_fontStyle)
        font.setPointSize(20)
        self.out0.setFont(font)
        self.out0.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.out0.setStyleSheet(css_sim_output_text)
        self.out0.setAlignment(QtCore.Qt.AlignCenter)
        self.out0.setObjectName("out0")
        self.sim_output_text_grid.addWidget(self.out0, 2, 2, 1, 1)

        # ---> Sim: Output 01 <--- #
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.out1.sizePolicy().hasHeightForWidth())
        self.out1.setSizePolicy(sizePolicy)
        self.out1.setMinimumSize(QtCore.QSize(50, 50))
        self.out1.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily(css_fontStyle)
        font.setPointSize(20)
        self.out1.setFont(font)
        self.out1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.out1.setStyleSheet(css_sim_output_text)
        self.out1.setAlignment(QtCore.Qt.AlignCenter)
        self.out1.setObjectName("out1")
        self.sim_output_text_grid.addWidget(self.out1, 2, 3, 1, 1)

        # ---> Sim: Output 02 <--- #
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.out2.sizePolicy().hasHeightForWidth())
        self.out2.setSizePolicy(sizePolicy)
        self.out2.setMinimumSize(QtCore.QSize(50, 50))
        self.out2.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily(css_fontStyle)
        font.setPointSize(20)
        self.out2.setFont(font)
        self.out2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.out2.setStyleSheet(css_sim_output_text)
        self.out2.setAlignment(QtCore.Qt.AlignCenter)
        self.out2.setObjectName("out2")
        self.sim_output_text_grid.addWidget(self.out2, 2, 4, 1, 1)

        # ---> Sim: Output 03 <--- #
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.out3.sizePolicy().hasHeightForWidth())
        self.out3.setSizePolicy(sizePolicy)
        self.out3.setMinimumSize(QtCore.QSize(50, 50))
        self.out3.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily(css_fontStyle)
        font.setPointSize(20)
        self.out3.setFont(font)
        self.out3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.out3.setStyleSheet(css_sim_output_text)
        self.out3.setAlignment(QtCore.Qt.AlignCenter)
        self.out3.setObjectName("out3")
        self.sim_output_text_grid.addWidget(self.out3, 3, 2, 1, 1)

        # ---> Sim: Output 04 <--- #
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.out4.sizePolicy().hasHeightForWidth())
        self.out4.setSizePolicy(sizePolicy)
        self.out4.setMinimumSize(QtCore.QSize(50, 50))
        self.out4.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily(css_fontStyle)
        font.setPointSize(20)
        self.out4.setFont(font)
        self.out4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.out4.setStyleSheet(css_sim_output_text)
        self.out4.setAlignment(QtCore.Qt.AlignCenter)
        self.out4.setObjectName("out4")
        self.sim_output_text_grid.addWidget(self.out4, 3, 3, 1, 1)

        # ---> Sim: Output 05 <--- #
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.out5.sizePolicy().hasHeightForWidth())
        self.out5.setSizePolicy(sizePolicy)
        self.out5.setMinimumSize(QtCore.QSize(50, 50))
        self.out5.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily(css_fontStyle)
        font.setPointSize(20)
        self.out5.setFont(font)
        self.out5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.out5.setStyleSheet(css_sim_output_text)
        self.out5.setAlignment(QtCore.Qt.AlignCenter)
        self.out5.setObjectName("out5")
        self.sim_output_text_grid.addWidget(self.out5, 3, 4, 1, 1)

        # ---> Sim: Output 06 <--- #
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.out6.sizePolicy().hasHeightForWidth())
        self.out6.setSizePolicy(sizePolicy)
        self.out6.setMinimumSize(QtCore.QSize(50, 50))
        self.out6.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily(css_fontStyle)
        font.setPointSize(20)
        self.out6.setFont(font)
        self.out6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.out6.setStyleSheet(css_sim_output_text)
        self.out6.setAlignment(QtCore.Qt.AlignCenter)
        self.out6.setObjectName("out6")
        self.sim_output_text_grid.addWidget(self.out6, 4, 2, 1, 1)

        # ---> Sim: Output 07 <--- #
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.out7.sizePolicy().hasHeightForWidth())
        self.out7.setSizePolicy(sizePolicy)
        self.out7.setMinimumSize(QtCore.QSize(50, 50))
        self.out7.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily(css_fontStyle)
        font.setPointSize(20)
        self.out7.setFont(font)
        self.out7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.out7.setStyleSheet(css_sim_output_text)
        self.out7.setAlignment(QtCore.Qt.AlignCenter)
        self.out7.setObjectName("out7")
        self.sim_output_text_grid.addWidget(self.out7, 4, 3, 1, 1)

        # ---> Sim: Output 08 <--- #
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.out8.sizePolicy().hasHeightForWidth())
        self.out8.setSizePolicy(sizePolicy)
        self.out8.setMinimumSize(QtCore.QSize(50, 50))
        self.out8.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily(css_fontStyle)
        font.setPointSize(20)
        self.out8.setFont(font)
        self.out8.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.out8.setStyleSheet(css_sim_output_text)
        self.out8.setAlignment(QtCore.Qt.AlignCenter)
        self.out8.setObjectName("out8")
        self.sim_output_text_grid.addWidget(self.out8, 4, 4, 1, 1)

        self.simulation_grid.addWidget(self.output, 2, 0, 2, 2)

        # ---> Simulation section controls label <--- #
        self.sim_controls_label.setMinimumSize(QtCore.QSize(0, 20))
        self.sim_controls_label.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily(css_fontStyle)
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.sim_controls_label.setFont(font)
        self.sim_controls_label.setStyleSheet(css_sim_ctrl_label)
        self.sim_controls_label.setAlignment(QtCore.Qt.AlignCenter)
        self.sim_controls_label.setObjectName("label")
        self.simulation_grid.addWidget(self.sim_controls_label, 0, 0, 1, 2, QtCore.Qt.AlignHCenter)

        self.container_grid.addWidget(self.sim, 1, 0, 2, 2)

    def solutionSection(self) -> None:
        # ---> Solution Section <--- #
        self.solution.setAutoFillBackground(False)
        self.solution.setStyleSheet("border: none;")
        self.solution.setObjectName("solution")

        # ---> Solution's Layout <--- #
        self.verticalLayout.setObjectName("verticalLayout")

        # Solution's Label <--- #
        self.output_window_label.setMinimumSize(QtCore.QSize(0, 20))
        self.output_window_label.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily(css_fontStyle)
        font.setPointSize(10)
        self.output_window_label.setFont(font)
        self.output_window_label.setAlignment(QtCore.Qt.AlignCenter)
        self.output_window_label.setObjectName("output_window_label")
        self.verticalLayout.addWidget(self.output_window_label)

        # ---> Output's print Window <--- #
        self.printWindow.setStyleSheet(css_printWindow)
        self.printWindow.setObjectName("printWindow")
        self.verticalLayout.addWidget(self.printWindow)

        self.container_grid.addWidget(self.solution, 1, 2, 2, 1)

    def programControls(self) -> None:
        # ---> Program Control widget <--- #
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.control.sizePolicy().hasHeightForWidth())
        self.control.setSizePolicy(sizePolicy)
        self.control.setStyleSheet("")
        self.control.setObjectName("control")

        # ---> Program Control widget's action button grid <--- #
        self.action_button_layout.setContentsMargins(20, 20, 20, 20)
        self.action_button_layout.setSpacing(20)
        self.action_button_layout.setObjectName("action_button_layout")

        # ---> Program Control's action button grid label <--- #
        self.options.setMinimumSize(QtCore.QSize(0, 20))
        self.options.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily(css_fontStyle)
        font.setPointSize(10)
        self.options.setFont(font)
        self.options.setAlignment(QtCore.Qt.AlignCenter)
        self.options.setObjectName("options")
        self.action_button_layout.addWidget(self.options, 0, 0, 1, 2)

        # ---> Program Control's find solution action button <--- #
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.findSolutionButton.sizePolicy().hasHeightForWidth())
        self.findSolutionButton.setSizePolicy(sizePolicy)
        self.findSolutionButton.setMinimumSize(QtCore.QSize(100, 50))
        self.findSolutionButton.setMaximumSize(QtCore.QSize(200, 100))
        self.findSolutionButton.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(css_fontStyle)
        font.setPointSize(10)
        self.findSolutionButton.setFont(font)
        self.findSolutionButton.setAutoFillBackground(False)
        self.findSolutionButton.setStyleSheet(css_buttons)
        self.findSolutionButton.setAutoDefault(True)
        self.findSolutionButton.setObjectName("findSolutionButton")
        self.action_button_layout.addWidget(self.findSolutionButton, 1, 0, 1, 1)

        # ---> Program Control's Is solvable action button <--- #
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.isSolvableButton.sizePolicy().hasHeightForWidth())
        self.isSolvableButton.setSizePolicy(sizePolicy)
        self.isSolvableButton.setMinimumSize(QtCore.QSize(100, 50))
        self.isSolvableButton.setMaximumSize(QtCore.QSize(200, 100))
        font = QtGui.QFont()
        font.setFamily(css_fontStyle)
        font.setPointSize(10)
        self.isSolvableButton.setFont(font)
        self.isSolvableButton.setStyleSheet(css_buttons)
        self.isSolvableButton.setShortcut("")
        self.isSolvableButton.setObjectName("isSolvableButton")
        self.action_button_layout.addWidget(self.isSolvableButton, 1, 1, 1, 1)

        # ---> Program Control's app reset action button <--- #
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.appResetButton.sizePolicy().hasHeightForWidth())
        self.appResetButton.setSizePolicy(sizePolicy)
        self.appResetButton.setMinimumSize(QtCore.QSize(100, 50))
        self.appResetButton.setMaximumSize(QtCore.QSize(200, 100))
        font = QtGui.QFont()
        font.setFamily(css_fontStyle)
        font.setPointSize(10)
        self.appResetButton.setFont(font)
        self.appResetButton.setStyleSheet(css_buttons)
        self.appResetButton.setAutoDefault(True)
        self.appResetButton.setObjectName("appResetButton")
        self.action_button_layout.addWidget(self.appResetButton, 2, 1, 1, 1)

        # ---> Program Control's Simulation action button <--- #
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.simulationButton.sizePolicy().hasHeightForWidth())
        self.simulationButton.setSizePolicy(sizePolicy)
        self.simulationButton.setMinimumSize(QtCore.QSize(100, 50))
        self.simulationButton.setMaximumSize(QtCore.QSize(200, 100))
        font = QtGui.QFont()
        font.setFamily(css_fontStyle)
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.simulationButton.setFont(font)
        self.simulationButton.setStyleSheet(css_buttons)
        self.simulationButton.setAutoDefault(True)
        self.simulationButton.setObjectName("simulationButton")
        self.action_button_layout.addWidget(self.simulationButton, 2, 0, 1, 1)

        self.container_grid.addWidget(self.control, 0, 2, 1, 1)
        self.gridLayout.addWidget(self.container, 0, 1, 1, 1)
        self.main_window.setCentralWidget(self.centralwidget)

    def menuBarWidget(self) -> None:
        # ---> Menu Bar Widget <--- #
        self.menubar.setGeometry(QtCore.QRect(0, 0, 829, 21))
        self.menubar.setObjectName("menubar")

        # ---> Menu Bar options: Save <--- #
        self.settings.setObjectName("settings")
        self.main_window.setMenuBar(self.menubar)

        # ---> Menu Bar options:  <--- #
        self.statusbar.setObjectName("statusbar")
        self.main_window.setStatusBar(self.statusbar)

        # ---> Menu Bar option's Action : Save <--- #
        self.actionSave.setObjectName("actionSave")

        # ---> Menu Bar option's Action : Copy <--- #
        self.actionCopy.setObjectName("actionCopy")
        self.settings.addAction(self.actionSave)
        self.settings.addAction(self.actionCopy)
        self.menubar.addAction(self.settings.menuAction())
        self.retranslateUi()

    def tabOrderFunc(self) -> None:
        # ---> Setting Focus and Tab order <--- #
        QtCore.QMetaObject.connectSlotsByName(self.main_window)
        self.main_window.setTabOrder(self.i0, self.i1)
        self.main_window.setTabOrder(self.i1, self.i2)
        self.main_window.setTabOrder(self.i2, self.i3)
        self.main_window.setTabOrder(self.i3, self.i4)
        self.main_window.setTabOrder(self.i4, self.i5)
        self.main_window.setTabOrder(self.i5, self.i6)
        self.main_window.setTabOrder(self.i6, self.i7)
        self.main_window.setTabOrder(self.i7, self.i8)
        self.main_window.setTabOrder(self.i8, self.g0)
        self.main_window.setTabOrder(self.g0, self.g1)
        self.main_window.setTabOrder(self.g1, self.g2)
        self.main_window.setTabOrder(self.g2, self.g3)
        self.main_window.setTabOrder(self.g3, self.g4)
        self.main_window.setTabOrder(self.g4, self.g5)
        self.main_window.setTabOrder(self.g5, self.g6)
        self.main_window.setTabOrder(self.g6, self.g7)
        self.main_window.setTabOrder(self.g7, self.g8)
        self.main_window.setTabOrder(self.g8, self.findSolutionButton)
        self.main_window.setTabOrder(self.findSolutionButton, self.isSolvableButton)
        self.main_window.setTabOrder(self.isSolvableButton, self.simulationButton)
        self.main_window.setTabOrder(self.simulationButton, self.appResetButton)
        self.main_window.setTabOrder(self.appResetButton, self.previousButton)
        self.main_window.setTabOrder(self.previousButton, self.pauseButton)
        self.main_window.setTabOrder(self.pauseButton, self.startButton)
        self.main_window.setTabOrder(self.startButton, self.resetButton)
        self.main_window.setTabOrder(self.resetButton, self.nextButton)
        self.main_window.setTabOrder(self.nextButton, self.toggleManualButton)
        self.main_window.setTabOrder(self.toggleManualButton, self.printWindow)

        self.isSolvableButton.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.simulationButton.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.appResetButton.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.findSolutionButton.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.previousButton.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.pauseButton.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.toggleManualButton.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.nextButton.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.startButton.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.resetButton.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        self.isSolvableButton.clicked.connect(self.isSolvable)
        self.appResetButton.clicked.connect(self.resetALl)
        self.findSolutionButton.clicked.connect(self.findSolution)
        self.simulationButton.clicked.connect(self.simulation)
        self.toggleManualButton.clicked.connect(self.toggleManual)

        self.startButton.clicked.connect(self.startSim)
        self.pauseButton.clicked.connect(self.pauseSim)
        self.nextButton.clicked.connect(self.nextState)
        self.previousButton.clicked.connect(self.previousState)
        self.resetButton.clicked.connect(self.clearSimOut)

    def retranslateUi(self) -> None:
        _translate = QtCore.QCoreApplication.translate
        self.main_window.setWindowTitle(_translate("MainWindow", "8 Puzzle Solver"))
        self.goalLabel.setText(_translate("MainWindow", "Goal State"))
        self.toggleManualButton.setText(_translate("MainWindow", "Switch between states Manually"))
        self.nextButton.setText(_translate("MainWindow", "Next"))
        self.previousButton.setText(_translate("MainWindow", "Previous"))
        self.pauseButton.setText(_translate("MainWindow", "Pause"))
        self.resetButton.setText(_translate("MainWindow", "Reset"))
        self.startButton.setText(_translate("MainWindow", "Start"))
        self.out0.setText(_translate("MainWindow", ""))
        self.out1.setText(_translate("MainWindow", ""))
        self.out2.setText(_translate("MainWindow", ""))
        self.out3.setText(_translate("MainWindow", ""))
        self.out4.setText(_translate("MainWindow", ""))
        self.out5.setText(_translate("MainWindow", ""))
        self.out6.setText(_translate("MainWindow", ""))
        self.out7.setText(_translate("MainWindow", ""))
        self.out8.setText(_translate("MainWindow", ""))
        self.sim_controls_label.setText(_translate("MainWindow", "Simulation Controls"))
        self.output_window_label.setText(_translate("MainWindow", "Output Window!"))
        self.printWindow.setHtml(_translate("MainWindow",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    </p></body></html>"))
        self.options.setText(_translate("MainWindow", "Options"))
        self.isSolvableButton.setText(_translate("MainWindow", "Is Solvable?"))
        self.appResetButton.setText(_translate("MainWindow", "Reset"))
        self.findSolutionButton.setText(_translate("MainWindow", "Find Solution"))
        self.simulationButton.setText(_translate("MainWindow", "Simulation"))
        self.initLabel.setText(_translate("MainWindow", "Initial State"))
        self.settings.setTitle(_translate("MainWindow", "Settings"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow("dsd", MainWindow)
    ui.setupUi()
    MainWindow.show()
    sys.exit(app.exec_())
