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

def getDirection(direction):
    from game import Directions
    if direction is 'North':
        return Directions.NORTH
    elif direction is 'South':
        return Directions.SOUTH
    elif direction is 'East':
        return Directions.EAST
    elif direction is 'West':
        return Directions.WEST

def pushToFringe(fringe, nodeTuple, heuristicCost=None):
    if isinstance(fringe, util.PriorityQueue):
        totalCost = nodeTuple[0][2]

        for parent in nodeTuple[1]:
            if len(parent) == 3:
                totalCost += parent[2]

        if heuristicCost != None:
            totalCost += heuristicCost

        fringe.push(nodeTuple, totalCost)
    else:
        fringe.push(nodeTuple)

def genericSearch(problem, fringe, heuristic=None):
    for successor in problem.getSuccessors(problem.getStartState()):
        successorTuple = (successor, [problem.getStartState()])
        heuristicCost = None if heuristic == None else heuristic(successor[0], problem)
        pushToFringe(fringe, successorTuple, heuristicCost)

    goalStateTuple = None
    closedSet = [problem.getStartState()]

    while not fringe.isEmpty():
        print("")
        if not isinstance(fringe, util.PriorityQueue):
            print("Fringe Length:",len(fringe.list))
        parentTuple = fringe.pop()
        print("Top Fringe State:",parentTuple[0][0])
        print("Successors:",problem.getSuccessors(parentTuple[0][0]))
        print("Closed Set:", closedSet)
        
        if not (parentTuple[0][0] in closedSet):
            closedSet.append(parentTuple[0][0])
        else:
            continue

        if problem.isGoalState(parentTuple[0][0]):
            goalStateTuple = parentTuple
            break

        successors = problem.getSuccessors(parentTuple[0][0])
        
        for successor in successors:
            if successor[0] in closedSet:
                continue

            parentsList = parentTuple[1].copy()
            parentsList.insert(0, parentTuple[0])

            successorTuple = (successor, parentsList)
            heuristicCost = None if heuristic == None else heuristic(successor[0], problem)
            pushToFringe(fringe, successorTuple, heuristicCost)

    plan = []
    if goalStateTuple != None:
        parentList = goalStateTuple[1]
        parentList.insert(0, goalStateTuple[0])
        while len(parentList) > 0:
            parent = parentList.pop(0)
            if len(parent) == 3:
                plan.insert(0, getDirection(parent[1]))

    print("\nPlan:", plan, "\n")
    return plan

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
