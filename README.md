# PathQuest Lite <br>
## Minimum Cost Maze Solver using Dijkastra's Algorithm<br>
<br>
<br>
PathQuest Lite is a Python program that finds the minimum-cost path in a maze using Dijkstra's Algorithm. The maze contains walls, traps, monsters, a start node, and an end node. The solver computes the least-cost route while avoiding obstacles.<br>
<br>

## Problem Statement
Build PathQuest Lite, a maze-solving program that finds the minimum-cost path from S (Start) to E (End).<br>
<br>
The maze may contain:
<br>
- S – Start<br>
- E – End<br>
- . – Empty path<br>
- T – Traps (extra cost)<br>
- M – Monsters (higher cost)<br>
- # – Walls (blocked)<br>
<br>
Use Dijkstra's Algorithm (or another suitable shortest-path algorithm) to compute the optimal path.<br>
<br>
<br>

## objective 
- Generate random mazes with different sizes.<br>
- Implement an efficient maze solver.<br>
- Compute and print the minimum cost to reach the destination.<br>
- Test your solution on multiple randomly generated mazes.<br>
- Organize your code into clean, modular functions.<br>
<br>
<br>

## Features 
-Random maze generation<br>
-Graph representation<br>
-Dijkastra Algorithm<br>
-Minimum-cost path<br>
-Trap cells<br>
-Monster cells count<br>
-Walls<br>
-Path reconstruction<br>
<br>
<br>

## Technologies used
-Python 3<br>
-random<br>
-heapq<br>
-collections<br>
-VS Code<br>

## cells cost
<br>
Cell                                       Cost<br>
S            -                               0<br>
E            -                               0<br>
.            -                               1<br>
T            -                               3<br>
M            -                               5<br>
#            -                               blocked<br>
<br>

## Project Structure
-main.py - Runs the project<br>
-maze_generator.py - Generates the maze<br>
-graph.py - Converts maze into a graph<br>
-pathfinder.py - finds the path<br>
<br>

## How to Run
<br>
Run : python main.py<br>
<br>

## Acknowledgement
Developed as part of WnCC Season of code 2026<br>

## Conclusion
PathQuest Lite successfully demonstrates how a maze can be represented as a graph and solved using Dijkstra's Algorithm to find the minimum-cost path from the start to the destination. The project combines concepts of graph theory, weighted shortest path algorithms, and Python programming in a practical application. Through this project, I gained experience in graph modelling, algorithm implementation, debugging, and writing modular code. Future improvements include adding a graphical user interface, maze visualization, support for larger mazes, and implementing alternative pathfinding algorithms such as A* for performance comparison.

