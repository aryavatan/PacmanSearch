# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    print("\n\n\n\n\nDepth-First Search:\n")
    fringe = util.Stack()
    return genericSearch(problem, fringe)

def breadthFirstSearch(problem):
    print("\n\n\n\n\nBreadth-First Search:\n")
    fringe = util.Queue()
    return genericSearch(problem, fringe)

def uniformCostSearch(problem):
    print("\n\n\n\n\nUniform-Cost Search:\n")
    fringe = util.PriorityQueue()
    return genericSearch(problem, fringe)

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    print("\n\n\n\n\nA* Search:\n")
    fringe = util.PriorityQueue()
    return genericSearch(problem, fringe, heuristic)

def pushToFringe(problem, fringe, nodeTuple, heuristicCost=None):
    # If fringe is priority queue, calculate the total cost from the starting node
    # to the current node tuple
    if isinstance(fringe, util.PriorityQueue):
        totalCost = problem.getCostOfActions(nodeTuple[1])

        # If heurisitic cost was provided, add that to the total cost
        if heuristicCost != None:
            totalCost += heuristicCost

        # Add node tuple to the fringe using the totalCost as the priority
        fringe.push(nodeTuple, totalCost)
    else:
        fringe.push(nodeTuple)

def genericSearch(problem, fringe, heuristic=None):
    # The starting state of the problem
    startState = problem.getStartState()
    
    # The set of nodes already visited
    closedSet = []
    
    # The list of actions that lead the agent from the start to the goal
    plan = []

    # Push the starting state as well as an empty plan into the fringe as a nodeTuple
    # Heuristic cost will be calculated if a heurisitic function was provided
    nodeTuple = (startState, plan)
    heuristicCost = None if heuristic == None else heuristic(startState, problem)
    pushToFringe(problem, fringe, nodeTuple, heuristicCost)

    while not fringe.isEmpty(): 
        nodeTuple, plan = fringe.pop()
        
        # Don't evaluate a node that has already been visited
        if not nodeTuple in closedSet:
            closedSet.append(nodeTuple)

            if problem.isGoalState(nodeTuple):
                return plan
            
            successors = problem.getSuccessors(nodeTuple)

            for successor in successors:
                # For every successor, get the list of actions that led the agent from the start to this successor
                successorPlan = plan.copy()
                successorPlan.append(successor[1])
                
                # Create new node tuple for this successor using its state as well as its plan
                # Heuristic cost will be calculated if a heurisitic function was provided
                successorTuple = (successor[0], successorPlan)
                heuristicCost = None if heuristic == None else heuristic(successor[0], problem)
                pushToFringe(problem, fringe, successorTuple, heuristicCost)
    
    # If goal was not achieved return empty plan
    return []

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
