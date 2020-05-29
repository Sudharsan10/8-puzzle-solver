<meta name="google-site-verification" content="anaQPdlDO5QzFwQQ6mpEFvfJXLj2Ue8-EFylgHd7JlU" />

<p align="center">
  <a href="https://github.com/Sudharsan10/TilePuzzelSolver-App">
    <img src=".\img\project_social_card01.png" alt="Social-header">
  </a>  
</p>

<p align="center">
  An 8 Tile Puzzle solver app.  
  <br>
    <a href=""><strong>Explore 8 Tile Puzzle solver app docs »</strong></a>
    <br>
    <br>
    <a href="https://github.com/Sudharsan10/TilePuzzelSolver-App/issues/new">Report bug</a>
    ·
    <a href="https://github.com/Sudharsan10/TilePuzzelSolver-App/issues/new">Request feature</a>    
</p>


8 Puzzle solver is a basic app to perform brute force search coupled with breadth first search algorithm to find solution 
to a given 8 tile puzzle configuration.
## Work in progress
- [ ] Replace GUI with better UI design and styles.
- [ ] Add documentation for Solver and project
- [ ] Feat: add feature Save solution
- [ ] Feat: add feature load custom user puzzle from a .txt file
- [ ] add How to use app instructions

## Table of contents
- [Quick start](#quick-start)
- [Pre-Requisites](#pre-requisites)
- [Run instructions](#run-instructions)
- [Status](#status)
- [What's included](#whats-included)
- [Bugs and Feature requests](#bugs-and-feature-requests)
- [Documentation](#documentation)
- [Creators](#creators)
- [Thanks](#thanks)

## Quick start
There are two ways to run this app: 
- [Download the latest Docker container.]() and run from the app in that container
- Clone the repo: 
    > ```
    > git clone https://github.com/Sudharsan10/TilePuzzelSolver-App.git
    > ```
    
## Status
[![Documentation Status](https://img.shields.io/badge/Documentation-yes-e01563)](https://github.com/Sudharsan10/TilePuzzelSolver-App/tree/master/img/logo)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-e01563.svg)](https://github.com/Sudharsan10/TilePuzzelSolver-App/graphs/commit-activity)
[![made-with-python](https://img.shields.io/badge/Python%20Version-3.8.3-brightgreen)](https://www.python.org/)
[![pip-version](https://img.shields.io/badge/pip%20Version-20.0.2-brightgreen)](https://pip.pypa.io/en/stable/installing/)
[![pyqt-version](https://img.shields.io/badge/PyQt5%20Version-5.14.2-brightgreen)](https://pypi.org/project/PyQt5/)
[![numpy-version](https://img.shields.io/badge/numpy%20Version-1.18.1-brightgreen)](https://pypi.org/project/numpy/)
[![made-with-Markdown](https://img.shields.io/badge/Made%20with-Markdown-0366d6.svg)](http://commonmark.org)
[![contributors](https://img.shields.io/badge/Contributors-01-0366d6)](https://github.com/Sudharsan10/TilePuzzelSolver-App/graphs/contributors)
[![Logo](https://img.shields.io/badge/Logo-Adobe%20Photoshop-20639B.svg)](https://github.com/Sudharsan10/TilePuzzelSolver-App/graphs/commit-activity)
[![Flow-charts](https://img.shields.io/badge/Flowcharts-MS%20Power%20Point-20639B.svg)](https://github.com/Sudharsan10/TilePuzzelSolver-App/graphs/commit-activity)
[![UI](https://img.shields.io/badge/GUI-PyQt5%20&%20CSS-FEBB13.svg)](https://github.com/Sudharsan10/TilePuzzelSolver-App/graphs/commit-activity)


## What's included
Within the download you'll find the following directories and files, logically grouping the modules in its own packages. 
You'll see something like this:

```text
TilePuzzleSolver/
├── controller/
|   ├── __init__.py
|   └── gui_controller.py   
├── data/
|   ├── __init__.py
|   └── ui_data.py 
├── docs/ ...
├── img/ ...
├── solver/
|   ├── __init__.py
|   ├── test_tile_puzzle_solver.py 
|   └── tile_puzzle_solver.py
├── ui/
|   ├── __init__.py
|   ├── css_styles.py  
|   ├── gui.py
|   └── TilePuzzleSolverGUI.ui
├── Readme.md
└── setup.py
```


## Pre-requisites
This app depends on ```numpy``` and ```PyQt5``` libraries. We can setup this up using pip installer or conda virtual environment tool.

- setting up using pip installer
    > ```
    > pip install numpy
    >```
    
    > ```
    > pip install PyQt5 
    Note: If you have both python2 and python3 installed replace ```pip``` with ```pip3``` when using python3. In case you need to install
    ```pip``` follow this [link](#https://pip.pypa.io/en/stable/installing/) to get ```pip``` setup before running the above commands.
    
- setting up using conda environment for ```python3```     
    > ```
    > conda install -c anaconda numpy
    >```
    
    > ```
    > conda install -c anaconda pyqt
    > ```
    Note: To install and setup anaconda environment follow this [link](#https://docs.anaconda.com/anaconda/install/) first and visit this section again after successfully setting up the conda environment.

## Run instructions
To run the app, first finish the pre-requisites mentioned, then
1. Clone the repo in terminal using following command: 
    > ```
    > git clone https://github.com/Sudharsan10/TilePuzzelSolver-App.git
    > ```
    or download github repo as ```.zip``` and extract it in the desired location.
    
2. In terminal navigate to the root folder abd locate the ```setup.py``` file and run the following command:
    > ```
    > python setup.py
    > ```

If every requirement is fulfilled a window should open as follow,

<p align="center;">
    <a href="https://github.com/Sudharsan10/TilePuzzelSolver-App">
    <img src=".\img\ui\start_screen.png" alt="start-screen">
    </a>
</p>




## Bugs and feature requests
Have a bug or a feature request? Search for existing and closed issues, if your problem or idea is not addressed yet, 
[please open a new issue](https://github.com/Sudharsan10/TilePuzzelSolver-App/issues/new).

## Documentation
Working on documentation stay tuned!


## Creators
**@Sudharsan** : <https://github.com/Sudharsan10>

<p align='center'>
    <a id='thanks'></a>
    Thank you for visiting our Repo!
</p>
