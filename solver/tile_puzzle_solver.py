"""
# ------------------------------------------------------------------------------------------------ #
# Project   :-> 8 Tile Puzzle solver
# Authors   :-> Sudharsan
# E-mail    :-> sudharsansci@gmail.com
# ------------------------------------------------------------------------------------------------ #
"""
# ------------------------------------------------------------------------------------------------ #
# Import Section for Importing library
# ------------------------------------------------------------------------------------------------ #
from queue import Queue
import numpy as np


# ------------------------------------------------------------------------------------------------ #
# Class for the solver Algorithm
# ------------------------------------------------------------------------------------------------ #
class Node:
    """
    Custom made data structure for storing Node info using class Node.
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
    """
    A 8 tile puzzle solver class with adequate methods

    Attributes:
        -> init_state               :-> Initial State of the given puzzle
        -> init_id                  :-> Unique number based on puzzle's Initial state
        -> goal_state               :-> Goal State of the given puzzle
        -> goal_id                  :-> Unique number based on puzzle's Goal state
        -> neighbours               :-> neighbor location map for each tile location in puzzle
        -> que                      :-> A deque object to implement FIFO logic for Breadth first
                                        search Algorithm
        -> nodes                    :-> A dictionary with node object as value and node's id as key
        -> current_node             :-> generate a node object based on initial state of puzzle
        -> exit_flag                :-> True if goal is found, False by default
        -> solvable                 :-> True if the puzzle is solvable, else False


    static methods:
        -> isSolvable               :-> Checks the solution feasibility of the puzzle
        -> generateUniqueNumber     :-> generates a unique number based on the puzzle's current state

    methods:
        -> __init__()               :-> Initializes the attributes
        -> findNeighbors            :-> finds the possible moves based on puzzle's current state
        -> findChildStates          :-> finds the new states based on the moves possible
        -> backTrack                :-> based on the node id back tracks back to the start node and
                                        returns the solution
        -> bruteForceExplorationBFS :-> A function to implement brute force search using breadth
                                        first search algorithm
        -> autoSolve                :-> Calls all the necessary function upon obj creation and
                                        solves and returns the solution

    """

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
        self.solvable = self.isSolvable(self.init_state.tolist(), self.goal_state.tolist())
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

        It takes the initial state and goal state unique number and checks for solution
        feasibility.

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

        # initialize Miscellaneous variable
        n = len(init)

        for i in range(0, n):
            if i not in init or i not in goal:
                return False

        # ---> Step 02: Remove zero from the args <--- #
        init.remove(0)
        goal.remove(0)

        # ---> Step 03: Initialize flip counter <---#
        init_flip_count, goal_flip_count = 0, 0

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
    def generateUniqueNumber(node: np.array, unique_seq: np.array = np.array(
        [100000000, 10000000, 1000000, 100000, 10000, 1000, 100, 10, 1])) -> int:
        """
        Args:
            unique_seq: np.array
                np.array([100000000, 10000000, 1000000, 100000, 10000, 1000, 100, 10, 1])
                the multiplier
            node: np.array
                Its a 1D array

        Returns: int
                A 9 digit int

        """
        return node @ unique_seq

    def bruteForceExplorationBFS(self) -> bool:
        """
        This Function explores the possible states of the Tile Puzzle using breadth first
        search Algorithm
        Returns: bool
            Returns True if goal is found or else False.

        """
        while not self.que.empty() and not self.exit_flag:
            self.current_node = self.que.get()
            move = self.findNeighbors(self.current_node)
            self.findChildStates(move, self.current_node)

        return self.exit_flag

    def findNeighbors(self, node: Node) -> set:
        """
        A Function to get the possible neighbor index based on blank tile location
        Returns: None

        """
        return self.neighbours[node.blank_tile_index].difference(node.hist_blank_tile_index)

    def findChildStates(self, moves: set, node: Node) -> None:
        """
        Based on the moves available for current state, it generates new possible states.
        Args:
            node: Node
                its the current node object
            moves: set
                set of possible moves

        Returns:

        """
        parent_state = np.copy(node.current_state)
        parent_id = node.id
        index = node.blank_tile_index
        for move in moves:
            new_state = np.copy(parent_state)
            new_state[move], new_state[index] = parent_state[index], parent_state[move]
            unique_id = self.generateUniqueNumber(new_state)
            if unique_id not in self.nodes:
                child_node = Node(unique_id, new_state, move, parent_id, index)
                self.nodes[unique_id] = child_node
                if unique_id == self.goal_id:
                    self.exit_flag = True
                self.que.put(child_node)

    def backTrack(self, uniq_id: int = None) -> list:
        """

        Args:
            uniq_id: int
                Unique id of a node to start the back tracking

        Returns: list
            Returns a list containing the solution to the puzzle

        """
        if uniq_id is None:
            uniq_id = self.goal_id
        current_node = self.nodes[uniq_id]
        current_id = current_node.id
        path = [current_node.current_state]

        while current_id != current_node.parent_id:
            current_node = self.nodes[current_node.parent_id]
            path.append(current_node.current_state)
            current_id = current_node.id
        return path[::-1]

    def autoSolve(self) -> list:
        """
        In one function checks for solution feasibility, runs the
        bruteForceExplorationBFS() and backTrack() and returns the solution
        Returns: list
            Solution to the given puzzle
        """
        if self.solvable:
            self.bruteForceExplorationBFS()
            return self.backTrack(self.goal_id)
        else:
            return ["Not Solvable!"]