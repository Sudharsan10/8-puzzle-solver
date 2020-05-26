# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\TilePuzzleSolverGUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Ui_MainWindow(object):
    def __init__(self, controller: object):
        # ---> Attributes <--- #
        self.controller = controller

    def setupUi(self, MainWindow):
        # ---> Main Window Initialization<--- #
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(829, 744)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(700, 700))
        MainWindow.setAnimated(True)

        # ---> Central Widget Initialization<--- #
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(245, 245, 245);\n")
        self.centralwidget.setObjectName("centralwidget")

        # ---> Central Widget's Grid layout Initialization<--- #
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")

        # ---> Container Initialization<--- #
        self.container = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.container.sizePolicy().hasHeightForWidth())

        self.container.setSizePolicy(sizePolicy)
        self.container.setMaximumSize(QtCore.QSize(700, 700))
        self.container.setStyleSheet("")
        self.container.setObjectName("container")

        # ---> Container's Grid layout Initialization<--- #
        self.container_grid = QtWidgets.QGridLayout(self.container)
        self.container_grid.setContentsMargins(0, 0, 0, 0)
        self.container_grid.setSpacing(5)
        self.container_grid.setObjectName("container_grid")

        # ---> Initial Widget <--- #
        self.initial_state = QtWidgets.QWidget(self.container)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.initial_state.sizePolicy().hasHeightForWidth())
        self.initial_state.setSizePolicy(sizePolicy)
        self.initial_state.setStyleSheet("border: none;")
        self.initial_state.setObjectName("initial_state")

        # ---> Initial Widget layout<--- #
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.initial_state)
        self.horizontalLayout.setObjectName("horizontalLayout")

        # ---> Init Input Widget<--- #
        self.init = QtWidgets.QWidget(self.initial_state)
        self.init.setMinimumSize(QtCore.QSize(200, 200))
        self.init.setObjectName("init")

        # ---> Init Input Widget's Layout <--- #
        self.init_input_grid = QtWidgets.QGridLayout(self.init)
        self.init_input_grid.setObjectName("init_input_grid")



        self.initLabel = QtWidgets.QLabel(self.init)
        self.initLabel.setMinimumSize(QtCore.QSize(0, 20))
        self.initLabel.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.initLabel.setFont(font)
        self.initLabel.setTextFormat(QtCore.Qt.AutoText)
        self.initLabel.setScaledContents(False)
        self.initLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.initLabel.setObjectName("initLabel")
        self.init_input_grid.addWidget(self.initLabel, 1, 0, 1, 3)

        # ---> Init Input 00 <--- #
        self.i0 = QtWidgets.QLineEdit(self.init)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(22)
        self.i0.setFont(font)
        self.i0.setStyleSheet("background: #ffffff; \n border: 2px solid red;;")
        self.i0.setMaxLength(1)
        self.i0.setAlignment(QtCore.Qt.AlignCenter)
        self.i0.setObjectName("lineEdit")
        self.init_input_grid.addWidget(self.i0, 2, 0, 1, 1)

        # ---> Init Input 01 <--- #
        self.i1 = QtWidgets.QLineEdit(self.init)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(22)
        self.i1.setFont(font)
        self.i1.setAutoFillBackground(False)
        self.i1.setStyleSheet("background: #ffffff; \n border: 2px solid red;")
        self.i1.setMaxLength(1)
        self.i1.setAlignment(QtCore.Qt.AlignCenter)
        self.i1.setClearButtonEnabled(False)
        self.i1.setObjectName("i1")
        self.init_input_grid.addWidget(self.i1, 2, 1, 1, 1)

        # ---> Init Input 02 <--- #
        self.i2 = QtWidgets.QLineEdit(self.init)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(22)
        self.i2.setFont(font)
        self.i2.setAutoFillBackground(False)
        self.i2.setStyleSheet("background: #ffffff; \n border: 2px solid red;")
        self.i2.setMaxLength(1)
        self.i2.setAlignment(QtCore.Qt.AlignCenter)
        self.i2.setClearButtonEnabled(False)
        self.i2.setObjectName("i2")
        self.init_input_grid.addWidget(self.i2, 2, 2, 1, 1)

        # ---> Init Input 03 <--- #
        self.i3 = QtWidgets.QLineEdit(self.init)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(22)
        self.i3.setFont(font)
        self.i3.setAutoFillBackground(False)
        self.i3.setStyleSheet("background: #ffffff; \n border: 2px solid red;;")
        self.i3.setMaxLength(1)
        self.i3.setAlignment(QtCore.Qt.AlignCenter)
        self.i3.setClearButtonEnabled(False)
        self.i3.setObjectName("i3")
        self.init_input_grid.addWidget(self.i3, 3, 0, 1, 1)

        # ---> Init Input 04 <--- #
        self.i4 = QtWidgets.QLineEdit(self.init)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(22)
        self.i4.setFont(font)
        self.i4.setAutoFillBackground(False)
        self.i4.setStyleSheet("background: #ffffff; \n border: 2px solid red;")
        self.i4.setMaxLength(1)
        self.i4.setAlignment(QtCore.Qt.AlignCenter)
        self.i4.setClearButtonEnabled(False)
        self.i4.setObjectName("i4")
        self.init_input_grid.addWidget(self.i4, 3, 1, 1, 1)

        # ---> Init Input 05 <--- #
        self.i5 = QtWidgets.QLineEdit(self.init)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(22)
        self.i5.setFont(font)
        self.i5.setAutoFillBackground(False)
        self.i5.setStyleSheet("background: #ffffff; \n border: 2px solid red;")
        self.i5.setMaxLength(1)
        self.i5.setAlignment(QtCore.Qt.AlignCenter)
        self.i5.setClearButtonEnabled(False)
        self.i5.setObjectName("i5")
        self.init_input_grid.addWidget(self.i5, 3, 2, 1, 1)

        # ---> Init Input 06 <--- #
        self.i6 = QtWidgets.QLineEdit(self.init)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(22)
        self.i6.setFont(font)
        self.i6.setAutoFillBackground(False)
        self.i6.setStyleSheet("background: #ffffff; \n border: 2px solid red;;")
        self.i6.setMaxLength(1)
        self.i6.setAlignment(QtCore.Qt.AlignCenter)
        self.i6.setClearButtonEnabled(False)
        self.i6.setObjectName("i6")
        self.init_input_grid.addWidget(self.i6, 4, 0, 1, 1)

        # ---> Init Input 07 <--- #
        self.i7 = QtWidgets.QLineEdit(self.init)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(22)
        self.i7.setFont(font)
        self.i7.setAutoFillBackground(False)
        self.i7.setStyleSheet("background: #ffffff; \n border: 2px solid red;;")
        self.i7.setMaxLength(1)
        self.i7.setAlignment(QtCore.Qt.AlignCenter)
        self.i7.setClearButtonEnabled(False)
        self.i7.setObjectName("i7")
        self.init_input_grid.addWidget(self.i7, 4, 1, 1, 1)

        # ---> Init Input 08 <--- #
        self.i8 = QtWidgets.QLineEdit(self.init)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(22)
        self.i8.setFont(font)
        self.i8.setAutoFillBackground(False)
        self.i8.setStyleSheet("background: #ffffff; \n border: 2px solid red;;")
        self.i8.setMaxLength(1)
        self.i8.setAlignment(QtCore.Qt.AlignCenter)
        self.i8.setClearButtonEnabled(False)
        self.i8.setObjectName("i8")
        self.init_input_grid.addWidget(self.i8, 4, 2, 1, 1)


        self.horizontalLayout.addWidget(self.init)
        self.container_grid.addWidget(self.initial_state, 0, 0, 1, 1)

        # ---> Goal Input Widget <--- #
        self.goal_state = QtWidgets.QWidget(self.container)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.goal_state.sizePolicy().hasHeightForWidth())
        self.goal_state.setSizePolicy(sizePolicy)
        self.goal_state.setStyleSheet("border: none;")
        self.goal_state.setObjectName("goal_state")

        # ---> Goal's grid <--- #
        self.gridLayout_5 = QtWidgets.QGridLayout(self.goal_state)
        self.gridLayout_5.setObjectName("gridLayout_5")

        # ---> Goal text grid Widget <--- #
        self.goal = QtWidgets.QWidget(self.goal_state)
        self.goal.setMinimumSize(QtCore.QSize(200, 200))
        self.goal.setObjectName("goal")

        # ---> Goal Input's grid <--- #
        self.goal_input_grid = QtWidgets.QGridLayout(self.goal)
        self.goal_input_grid.setObjectName("goal_input_grid")

        # ---> Goal Input 00 <--- #
        self.g0 = QtWidgets.QLineEdit(self.goal)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(22)
        self.g0.setFont(font)
        self.g0.setStyleSheet("background: #ffffff; border: 2px solid red;")
        self.g0.setMaxLength(1)
        self.g0.setAlignment(QtCore.Qt.AlignCenter)
        self.g0.setClearButtonEnabled(False)
        self.g0.setObjectName("g0")
        self.goal_input_grid.addWidget(self.g0, 2, 0, 1, 1)

        # ---> Goal Input 01 <--- #
        self.g1 = QtWidgets.QLineEdit(self.goal)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(22)
        self.g1.setFont(font)
        self.g1.setStyleSheet("background: #ffffff; border: 2px solid red;")
        self.g1.setMaxLength(1)
        self.g1.setAlignment(QtCore.Qt.AlignCenter)
        self.g1.setClearButtonEnabled(False)
        self.g1.setObjectName("g1")
        self.goal_input_grid.addWidget(self.g1, 2, 1, 1, 1)

        # ---> Goal Input 02 <--- #
        self.g2 = QtWidgets.QLineEdit(self.goal)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(22)
        self.g2.setFont(font)
        self.g2.setStyleSheet("background: #ffffff; border: 2px solid red;")
        self.g2.setMaxLength(1)
        self.g2.setAlignment(QtCore.Qt.AlignCenter)
        self.g2.setClearButtonEnabled(False)
        self.g2.setObjectName("g2")
        self.goal_input_grid.addWidget(self.g2, 2, 2, 1, 1)

        # ---> Goal Input 03 <--- #
        self.g3 = QtWidgets.QLineEdit(self.goal)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(22)
        self.g3.setFont(font)
        self.g3.setStyleSheet("background: #ffffff; border: 2px solid red;")
        self.g3.setMaxLength(1)
        self.g3.setAlignment(QtCore.Qt.AlignCenter)
        self.g3.setClearButtonEnabled(False)
        self.g3.setObjectName("g3")
        self.goal_input_grid.addWidget(self.g3, 3, 0, 1, 1)

        # ---> Goal Input 04 <--- #
        self.g4 = QtWidgets.QLineEdit(self.goal)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(22)
        self.g4.setFont(font)
        self.g4.setStyleSheet("background: #ffffff; border: 2px solid red;")
        self.g4.setMaxLength(1)
        self.g4.setAlignment(QtCore.Qt.AlignCenter)
        self.g4.setClearButtonEnabled(False)
        self.g4.setObjectName("g4")
        self.goal_input_grid.addWidget(self.g4, 3, 1, 1, 1)

        # ---> Goal Input 05 <--- #
        self.g5 = QtWidgets.QLineEdit(self.goal)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(22)
        self.g5.setFont(font)
        self.g5.setStyleSheet("background: #ffffff; border: 2px solid red;")
        self.g5.setMaxLength(1)
        self.g5.setAlignment(QtCore.Qt.AlignCenter)
        self.g5.setClearButtonEnabled(False)
        self.g5.setObjectName("g5")
        self.goal_input_grid.addWidget(self.g5, 3, 2, 1, 1)

        # ---> Goal Input 06 <--- #
        self.g6 = QtWidgets.QLineEdit(self.goal)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(22)
        self.g6.setFont(font)
        self.g6.setStyleSheet("background: #ffffff; border: 2px solid red;")
        self.g6.setMaxLength(1)
        self.g6.setAlignment(QtCore.Qt.AlignCenter)
        self.g6.setClearButtonEnabled(False)
        self.g6.setObjectName("g6")
        self.goal_input_grid.addWidget(self.g6, 4, 0, 1, 1)

        # ---> Goal Input 07 <--- #
        self.g7 = QtWidgets.QLineEdit(self.goal)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(22)
        self.g7.setFont(font)
        self.g7.setStyleSheet("background: #ffffff; border: 2px solid red;")
        self.g7.setMaxLength(1)
        self.g7.setAlignment(QtCore.Qt.AlignCenter)
        self.g7.setClearButtonEnabled(False)
        self.g7.setObjectName("g7")
        self.goal_input_grid.addWidget(self.g7, 4, 1, 1, 1)

        # ---> Goal Input 08 <--- #
        self.g8 = QtWidgets.QLineEdit(self.goal)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(22)
        self.g8.setFont(font)
        self.g8.setStyleSheet("background: #ffffff; border: 2px solid red;")
        self.g8.setMaxLength(1)
        self.g8.setAlignment(QtCore.Qt.AlignCenter)
        self.g8.setClearButtonEnabled(False)
        self.g8.setObjectName("g8")
        self.goal_input_grid.addWidget(self.g8, 4, 2, 1, 1)

        # ---> Goal Widget Label <--- #
        self.goalLabel = QtWidgets.QLabel(self.goal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.goalLabel.sizePolicy().hasHeightForWidth())
        self.goalLabel.setSizePolicy(sizePolicy)
        self.goalLabel.setMinimumSize(QtCore.QSize(40, 20))
        self.goalLabel.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.goalLabel.setFont(font)
        self.goalLabel.setScaledContents(False)
        self.goalLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.goalLabel.setObjectName("goalLabel")
        self.goal_input_grid.addWidget(self.goalLabel, 1, 0, 1, 3)

        self.gridLayout_5.addWidget(self.goal, 0, 0, 1, 1)
        self.container_grid.addWidget(self.goal_state, 0, 1, 1, 1)

        # ---> Simulation Widget <--- #
        self.sim = QtWidgets.QWidget(self.container)
        self.sim.setAutoFillBackground(False)
        self.sim.setStyleSheet("border: none;")
        self.sim.setObjectName("sim")

        # ---> Simulation Widget's Grid <--- #
        self.simulationt_grid = QtWidgets.QGridLayout(self.sim)
        self.simulationt_grid.setObjectName("simulationt_grid")

        # ---> Simulation Widget's control Widget <--- #
        self.controls = QtWidgets.QWidget(self.sim)
        self.controls.setMinimumSize(QtCore.QSize(0, 137))
        self.controls.setObjectName("controls")

        # ---> Simulation control Widget's grid <--- #
        self.sim_controls_grid = QtWidgets.QGridLayout(self.controls)
        self.sim_controls_grid.setObjectName("sim_controls_grid")

        # ---> Sim control's toggle manual control button <--- #
        self.toggleManualControl = QtWidgets.QPushButton(self.controls)
        self.toggleManualControl.setMinimumSize(QtCore.QSize(0, 30))
        self.toggleManualControl.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.toggleManualControl.setFont(font)
        self.toggleManualControl.setStyleSheet("background: #00aaff;\n color:white;\n border-style: outset;\n border-width: 1px;\n border-radius: 15px;\n border-color: black;\n padding: 4px;")
        self.toggleManualControl.setAutoRepeat(False)
        self.toggleManualControl.setObjectName("toggleManualControl")
        self.sim_controls_grid.addWidget(self.toggleManualControl, 1, 1, 1, 3)

        # ---> Sim control's next state button <--- #
        self.nextButton = QtWidgets.QPushButton(self.controls)
        self.nextButton.setMinimumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.nextButton.setFont(font)
        self.nextButton.setStyleSheet("background: #00aaff;\n color:white;\n border-style: outset;\n border-width: 1px;\n border-radius: 15px;\n border-color: black;\n padding: 4px;")
        self.nextButton.setAutoRepeat(False)
        self.nextButton.setObjectName("nextButton")
        self.sim_controls_grid.addWidget(self.nextButton, 0, 4, 1, 1)

        # ---> Sim control's previous state button <--- #
        self.previousButton = QtWidgets.QPushButton(self.controls)
        self.previousButton.setMinimumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.previousButton.setFont(font)
        self.previousButton.setStyleSheet("background: #00aaff;\n color:white;\n border-style: outset;\n border-width: 1px;\n border-radius: 15px;\n border-color: black;\n padding: 4px;")
        self.previousButton.setAutoRepeat(False)
        self.previousButton.setObjectName("previousButton")
        self.sim_controls_grid.addWidget(self.previousButton, 0, 0, 1, 1)

        # ---> Sim control's pause button <--- #
        self.pauseButton = QtWidgets.QPushButton(self.controls)
        self.pauseButton.setMinimumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.pauseButton.setFont(font)
        self.pauseButton.setStyleSheet("background: #00aaff;\n color:white;\n border-style: outset;\n border-width: 1px;\n border-radius: 15px;\n border-color: black;\n padding: 4px;")
        self.pauseButton.setAutoRepeat(False)
        self.pauseButton.setObjectName("pauseButton")
        self.sim_controls_grid.addWidget(self.pauseButton, 0, 1, 1, 1)

        # ---> Sim control's reset button <--- #
        self.resetButton = QtWidgets.QPushButton(self.controls)
        self.resetButton.setMinimumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.resetButton.setFont(font)
        self.resetButton.setStyleSheet("background: #00aaff;\n color:white;\n border-style: outset;\n border-width: 1px;\n border-radius: 15px;\n border-color: black;\n padding: 4px;")
        self.resetButton.setAutoRepeat(False)
        self.resetButton.setObjectName("resetButton")
        self.sim_controls_grid.addWidget(self.resetButton, 0, 3, 1, 1)

        # ---> Sim control's start button <--- #
        self.startButton = QtWidgets.QPushButton(self.controls)
        self.startButton.setMinimumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.startButton.setFont(font)
        self.startButton.setStyleSheet("background: #00aaff;\n color:white;\n border-style: outset;\n border-width: 1px;\n border-radius: 15px;\n border-color: black;\n padding: 4px;")
        self.startButton.setAutoRepeat(False)
        self.startButton.setObjectName("startButton")
        self.sim_controls_grid.addWidget(self.startButton, 0, 2, 1, 1)

        self.simulationt_grid.addWidget(self.controls, 1, 0, 1, 2)

        # ---> Simulation solution output widget <--- #
        self.output = QtWidgets.QWidget(self.sim)
        self.output.setObjectName("output")

        # --->  Sim output text grid <--- #
        self.sim_output_text_grid = QtWidgets.QGridLayout(self.output)
        self.sim_output_text_grid.setHorizontalSpacing(5)
        self.sim_output_text_grid.setVerticalSpacing(30)
        self.sim_output_text_grid.setObjectName("sim_output_text_grid")

        # ---> Sim: Output 00 <--- #
        self.out0 = QtWidgets.QLabel(self.output)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.out0.sizePolicy().hasHeightForWidth())
        self.out0.setSizePolicy(sizePolicy)
        self.out0.setMinimumSize(QtCore.QSize(50, 50))
        self.out0.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(20)
        self.out0.setFont(font)
        self.out0.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.out0.setStyleSheet("background: #ffffff;\n border: 3px solid red;")
        self.out0.setAlignment(QtCore.Qt.AlignCenter)
        self.out0.setObjectName("out0")
        self.sim_output_text_grid.addWidget(self.out0, 2, 2, 1, 1)

        # ---> Sim: Output 01 <--- #
        self.out1 = QtWidgets.QLabel(self.output)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.out1.sizePolicy().hasHeightForWidth())
        self.out1.setSizePolicy(sizePolicy)
        self.out1.setMinimumSize(QtCore.QSize(50, 50))
        self.out1.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(20)
        self.out1.setFont(font)
        self.out1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.out1.setStyleSheet("background: #ffffff;\n border: 3px solid red;")
        self.out1.setAlignment(QtCore.Qt.AlignCenter)
        self.out1.setObjectName("out1")
        self.sim_output_text_grid.addWidget(self.out1, 2, 3, 1, 1)

        # ---> Sim: Output 02 <--- #
        self.out2 = QtWidgets.QLabel(self.output)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.out2.sizePolicy().hasHeightForWidth())
        self.out2.setSizePolicy(sizePolicy)
        self.out2.setMinimumSize(QtCore.QSize(50, 50))
        self.out2.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(20)
        self.out2.setFont(font)
        self.out2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.out2.setStyleSheet("background: #ffffff;\n border: 3px solid red;")
        self.out2.setAlignment(QtCore.Qt.AlignCenter)
        self.out2.setObjectName("out2")
        self.sim_output_text_grid.addWidget(self.out2, 2, 4, 1, 1)

        # ---> Sim: Output 03 <--- #
        self.out3 = QtWidgets.QLabel(self.output)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.out3.sizePolicy().hasHeightForWidth())
        self.out3.setSizePolicy(sizePolicy)
        self.out3.setMinimumSize(QtCore.QSize(50, 50))
        self.out3.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(20)
        self.out3.setFont(font)
        self.out3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.out3.setStyleSheet("background: #ffffff;\n border: 3px solid red;")
        self.out3.setAlignment(QtCore.Qt.AlignCenter)
        self.out3.setObjectName("out3")
        self.sim_output_text_grid.addWidget(self.out3, 3, 2, 1, 1)

        # ---> Sim: Output 04 <--- #
        self.out4 = QtWidgets.QLabel(self.output)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.out4.sizePolicy().hasHeightForWidth())
        self.out4.setSizePolicy(sizePolicy)
        self.out4.setMinimumSize(QtCore.QSize(50, 50))
        self.out4.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(20)
        self.out4.setFont(font)
        self.out4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.out4.setStyleSheet("background: #ffffff;\n border: 3px solid red;")
        self.out4.setAlignment(QtCore.Qt.AlignCenter)
        self.out4.setObjectName("out4")
        self.sim_output_text_grid.addWidget(self.out4, 3, 3, 1, 1)

        # ---> Sim: Output 05 <--- #
        self.out5 = QtWidgets.QLabel(self.output)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.out5.sizePolicy().hasHeightForWidth())
        self.out5.setSizePolicy(sizePolicy)
        self.out5.setMinimumSize(QtCore.QSize(50, 50))
        self.out5.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(20)
        self.out5.setFont(font)
        self.out5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.out5.setStyleSheet("background: #ffffff;\n border: 3px solid red;")
        self.out5.setAlignment(QtCore.Qt.AlignCenter)
        self.out5.setObjectName("out5")
        self.sim_output_text_grid.addWidget(self.out5, 3, 4, 1, 1)

        # ---> Sim: Output 06 <--- #
        self.out6 = QtWidgets.QLabel(self.output)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.out6.sizePolicy().hasHeightForWidth())
        self.out6.setSizePolicy(sizePolicy)
        self.out6.setMinimumSize(QtCore.QSize(50, 50))
        self.out6.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(20)
        self.out6.setFont(font)
        self.out6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.out6.setStyleSheet("background: #ffffff;\n border: 3px solid red;")
        self.out6.setAlignment(QtCore.Qt.AlignCenter)
        self.out6.setObjectName("out6")
        self.sim_output_text_grid.addWidget(self.out6, 4, 2, 1, 1)

        # ---> Sim: Output 07 <--- #
        self.out7 = QtWidgets.QLabel(self.output)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.out7.sizePolicy().hasHeightForWidth())
        self.out7.setSizePolicy(sizePolicy)
        self.out7.setMinimumSize(QtCore.QSize(50, 50))
        self.out7.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(20)
        self.out7.setFont(font)
        self.out7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.out7.setStyleSheet("background: #ffffff;\n border: 3px solid red;")
        self.out7.setAlignment(QtCore.Qt.AlignCenter)
        self.out7.setObjectName("out7")
        self.sim_output_text_grid.addWidget(self.out7, 4, 3, 1, 1)

        # ---> Sim: Output 08 <--- #
        self.out8 = QtWidgets.QLabel(self.output)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.out8.sizePolicy().hasHeightForWidth())
        self.out8.setSizePolicy(sizePolicy)
        self.out8.setMinimumSize(QtCore.QSize(50, 50))
        self.out8.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(20)
        self.out8.setFont(font)
        self.out8.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.out8.setStyleSheet("background: #ffffff;\n border: 3px solid red;")
        self.out8.setAlignment(QtCore.Qt.AlignCenter)
        self.out8.setObjectName("out8")
        self.sim_output_text_grid.addWidget(self.out8, 4, 4, 1, 1)

        self.simulationt_grid.addWidget(self.output, 2, 0, 2, 2)
        
        # ---> Simulation section controls label <--- #
        self.sim_controls_label = QtWidgets.QLabel(self.sim)
        self.sim_controls_label.setMinimumSize(QtCore.QSize(0, 20))
        self.sim_controls_label.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.sim_controls_label.setFont(font)
        self.sim_controls_label.setStyleSheet("font: 10pt \"Arial Rounded MT Bold\";\n text-align: center;\n")
        self.sim_controls_label.setAlignment(QtCore.Qt.AlignCenter)
        self.sim_controls_label.setObjectName("label")
        self.simulationt_grid.addWidget(self.sim_controls_label, 0, 0, 1, 2, QtCore.Qt.AlignHCenter)

        self.container_grid.addWidget(self.sim, 1, 0, 2, 2)

        # ---> Solution Section <--- #
        self.solution = QtWidgets.QWidget(self.container)
        self.solution.setAutoFillBackground(False)
        self.solution.setStyleSheet("border: none;")
        self.solution.setObjectName("solution")

        # ---> Solution's Layout <--- #
        self.verticalLayout = QtWidgets.QVBoxLayout(self.solution)
        self.verticalLayout.setObjectName("verticalLayout")

        # Solution's Label <--- #
        self.output_window_label = QtWidgets.QLabel(self.solution)
        self.output_window_label.setMinimumSize(QtCore.QSize(0, 20))
        self.output_window_label.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.output_window_label.setFont(font)
        self.output_window_label.setAlignment(QtCore.Qt.AlignCenter)
        self.output_window_label.setObjectName("output_window_label")
        self.verticalLayout.addWidget(self.output_window_label)

        # ---> Output's print Window <--- #
        self.printWindow = QtWidgets.QTextBrowser(self.solution)
        self.printWindow.setStyleSheet("background:#ffffff;\n text-align: center;\n border:1px solid black;\n")
        self.printWindow.setObjectName("printWindow")
        self.verticalLayout.addWidget(self.printWindow)
        
        self.container_grid.addWidget(self.solution, 1, 2, 2, 1)

        self.control = QtWidgets.QWidget(self.container)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.control.sizePolicy().hasHeightForWidth())
        self.control.setSizePolicy(sizePolicy)
        self.control.setStyleSheet("")
        self.control.setObjectName("control")

        self.action_button_layout = QtWidgets.QGridLayout(self.control)
        self.action_button_layout.setContentsMargins(20, 20, 20, 20)
        self.action_button_layout.setSpacing(20)
        self.action_button_layout.setObjectName("action_button_layout")


        self.options = QtWidgets.QLabel(self.control)
        self.options.setMinimumSize(QtCore.QSize(0, 20))
        self.options.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.options.setFont(font)
        self.options.setAlignment(QtCore.Qt.AlignCenter)
        self.options.setObjectName("options")
        self.action_button_layout.addWidget(self.options, 0, 0, 1, 2)


        self.isSolvableButton = QtWidgets.QPushButton(self.control)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.isSolvableButton.sizePolicy().hasHeightForWidth())
        self.isSolvableButton.setSizePolicy(sizePolicy)
        self.isSolvableButton.setMinimumSize(QtCore.QSize(100, 50))
        self.isSolvableButton.setMaximumSize(QtCore.QSize(200, 100))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.isSolvableButton.setFont(font)
        self.isSolvableButton.setStyleSheet("background-color:#00aaff;\n color:#ffffff;\n border-style: outset;\n border-width: 1px;\n border-radius: 15px;\n border-color: black;\n padding: 4px;")
        self.isSolvableButton.setShortcut("")
        self.isSolvableButton.setObjectName("isSolvableButton")
        self.action_button_layout.addWidget(self.isSolvableButton, 1, 1, 1, 1)


        self.appResetButton = QtWidgets.QPushButton(self.control)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.appResetButton.sizePolicy().hasHeightForWidth())
        self.appResetButton.setSizePolicy(sizePolicy)
        self.appResetButton.setMinimumSize(QtCore.QSize(100, 50))
        self.appResetButton.setMaximumSize(QtCore.QSize(200, 100))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.appResetButton.setFont(font)
        self.appResetButton.setStyleSheet("background-color:#00aaff;\n color:#ffffff;\n border-style: outset;\n border-width: 1px;\n border-radius: 15px;\n border-color: black;\n padding: 4px;")
        self.appResetButton.setAutoDefault(True)
        self.appResetButton.setObjectName("appResetButton")
        self.action_button_layout.addWidget(self.appResetButton, 2, 1, 1, 1)


        self.findSolutionButton = QtWidgets.QPushButton(self.control)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.findSolutionButton.sizePolicy().hasHeightForWidth())
        self.findSolutionButton.setSizePolicy(sizePolicy)
        self.findSolutionButton.setMinimumSize(QtCore.QSize(100, 50))
        self.findSolutionButton.setMaximumSize(QtCore.QSize(200, 100))
        self.findSolutionButton.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.findSolutionButton.setFont(font)
        self.findSolutionButton.setAutoFillBackground(False)
        self.findSolutionButton.setStyleSheet("background-color:#00aaff;\n color:#ffffff;\n border-style: outset;\n border-width: 1px;\n border-radius: 15px;\n border-color: black;\n padding: 4px;")
        self.findSolutionButton.setAutoDefault(True)
        self.findSolutionButton.setObjectName("findSolutionButton")
        self.action_button_layout.addWidget(self.findSolutionButton, 1, 0, 1, 1)


        self.simulationButton = QtWidgets.QPushButton(self.control)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.simulationButton.sizePolicy().hasHeightForWidth())
        self.simulationButton.setSizePolicy(sizePolicy)
        self.simulationButton.setMinimumSize(QtCore.QSize(100, 50))
        self.simulationButton.setMaximumSize(QtCore.QSize(200, 100))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.simulationButton.setFont(font)
        self.simulationButton.setStyleSheet("background-color:#00aaff;\n color:#ffffff;\n border-style: outset;\n border-width: 1px;\n border-radius: 15px;\n border-color: black;\n padding: 4px;")
        self.simulationButton.setCheckable(True)
        self.simulationButton.setChecked(False)
        self.simulationButton.setAutoDefault(True)
        self.simulationButton.setObjectName("simulationButton")
        self.action_button_layout.addWidget(self.simulationButton, 2, 0, 1, 1)

        self.container_grid.addWidget(self.control, 0, 2, 1, 1)

        

        self.gridLayout.addWidget(self.container, 0, 1, 1, 1)
        
        MainWindow.setCentralWidget(self.centralwidget)

        # ---> Menu Bar Widget <--- #
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 829, 21))
        self.menubar.setObjectName("menubar")

        # ---> Menu Bar options: Save <--- #
        self.settings = QtWidgets.QMenu(self.menubar)
        self.settings.setObjectName("settings")
        MainWindow.setMenuBar(self.menubar)

        # ---> Menu Bar options:  <--- #
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # ---> Menu Bar option's Action : Save <--- #
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")

        # ---> Menu Bar option's Action : Copy <--- #
        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.settings.addAction(self.actionSave)
        self.settings.addAction(self.actionCopy)
        self.menubar.addAction(self.settings.menuAction())
        self.retranslateUi(MainWindow)

        # ---> Setting Focus and Tab order <--- #
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.i0, self.i1)
        MainWindow.setTabOrder(self.i1, self.i2)
        MainWindow.setTabOrder(self.i2, self.i3)
        MainWindow.setTabOrder(self.i3, self.i4)
        MainWindow.setTabOrder(self.i4, self.i5)
        MainWindow.setTabOrder(self.i5, self.i6)
        MainWindow.setTabOrder(self.i6, self.i7)
        MainWindow.setTabOrder(self.i7, self.i8)
        MainWindow.setTabOrder(self.i8, self.g0)
        MainWindow.setTabOrder(self.g0, self.g1)
        MainWindow.setTabOrder(self.g1, self.g2)
        MainWindow.setTabOrder(self.g2, self.g3)
        MainWindow.setTabOrder(self.g3, self.g4)
        MainWindow.setTabOrder(self.g4, self.g5)
        MainWindow.setTabOrder(self.g5, self.g6)
        MainWindow.setTabOrder(self.g6, self.g7)
        MainWindow.setTabOrder(self.g7, self.g8)
        MainWindow.setTabOrder(self.g8, self.findSolutionButton)
        MainWindow.setTabOrder(self.findSolutionButton, self.isSolvableButton)
        MainWindow.setTabOrder(self.isSolvableButton, self.simulationButton)
        MainWindow.setTabOrder(self.simulationButton, self.appResetButton)
        MainWindow.setTabOrder(self.appResetButton, self.previousButton)
        MainWindow.setTabOrder(self.previousButton, self.pauseButton)
        MainWindow.setTabOrder(self.pauseButton, self.startButton)
        MainWindow.setTabOrder(self.startButton, self.resetButton)
        MainWindow.setTabOrder(self.resetButton, self.nextButton)
        MainWindow.setTabOrder(self.nextButton, self.toggleManualControl)
        MainWindow.setTabOrder(self.toggleManualControl, self.printWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.goalLabel.setText(_translate("MainWindow", "Goal State"))
        self.toggleManualControl.setText(_translate("MainWindow", "Switch between states Manually"))
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
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow("dsd")
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
