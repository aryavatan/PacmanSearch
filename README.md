# PacmanSearch
 
In this project, the Pacman agent can find paths through his maze world, both to reach a particular location and to collect food efficiently. The Pacman agent uses general search algorithms (informed and uninformed) to efficiently determine a path to his goal. I found this project on Berkeley University's AI material while working through my own AI course at university.


## Depth-First Search

The depth-first search algorithm can quickly find a solution for:
* `python pacman.py -l tinyMaze -p SearchAgent`
* `python pacman.py -l mediumMaze -p SearchAgent`
* `python pacman.py -l bigMaze -z .5 -p SearchAgent`


## Breadth-First Search

The breadth-first search algorithm can quickly find a solution for:
* `python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs`
* `python pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5`


## Uniform-Cost Search

By changing the cost function, we can encourage Pacman to find different paths. For example, we can charge more for dangerous steps in ghost-ridden areas or less for steps in food-rich areas, and a rational Pacman agent will adjust its behavior in response.
The uniform-cost search algorithm can quickly find a solution for:
* `python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs`
* `python pacman.py -l mediumDottedMaze -p StayEastSearchAgent`
* `python pacman.py -l mediumScaryMaze -p StayWestSearchAgent`


## A* Search

The A* graph search is a general informed search algorithm, it takes into account the total cost to the current node, as well as a predicted remaining cost to the goal state (this predicted cost function is known as the heuristic function). 
Using the Manhattan distance function as the heuristic, the A* search algorithm can quickly find a solution for:
* `python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic`


## Finding All The Corners

In corner mazes, there are four dots, one in each corner. Our new search problem is to find the shortest path through the maze that touches all four corners (whether the maze actually has food there or not).

With the new CornersProblem implemented, the breadth-first search algorithm can quickly find a solution for:
* `python pacman.py -l tinyCorners -p SearchAgent -a fn=bfs,prob=CornersProblem`
* `python pacman.py -l mediumCorners -p SearchAgent -a fn=bfs,prob=CornersProblem`


## Corners Problem: Heuristic

The real power of A* will only be apparent with a more challenging search problem. 
With a new non-trivial, consistent heuristic for the CornersProblem, the A* search algorithm can quickly find a solution for:
* `python pacman.py -l mediumCorners -p AStarCornersAgent -z 0.5`


## Help

If Pacman moves too slowly for you, try the option `--frameTime 0`.

Note that pacman.py supports a number of options that can each be expressed in a long way (e.g., --layout) or a short way (e.g., -l). You can see the list of all options and their default values via:

* `python pacman.py -h`
