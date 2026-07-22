# Competitive Programming in python - (from begginer to contest level)

Mentor : Srinivas Dorisala<br>
Mentee : Shruti Vairagade<br>
<br>
Introduction:<br>
<br>
This repository contains my work completed during the first four week of the summer of code project (SoC) 2026 project on Competitive programming using python.
the aim of this project is to develop strong problem-solving skills, improve algorithmic thinking, and gain proficiecncy in implementing efficient solution
to programming challenges.<br>
<br>
<br>
Throughout the project, I practiced a variety of competitive programming concepts including complexity analysis, data structures, searching and sorting techniques,
recursion, and algorithmic problem-solving. The assignments and coding exercises helped me strengthen my understanding of python.<br>
<br>
<br>
This repository serves as a record of my progress, containing weekly assignments, solutions, and notes covering the topics learned during the first four weeks of the program<br>
<br>
<br>
Topics covered:<br>
<br>
1. Basics of python
2. Data structure of python
3. Sorting Algorithm
4. Searching algorithm
5. Recursion fundamentals
6. Basics of greedy and Backtracking
7. Time and space complexity
8. Graph Basics
9. Traversal - DFS & BFS
10. Cycle Detection
11. Topological sorting
12. Shortest Path algorithm (Dijkastra, Beliman-Ford, BFS)
13. Minimum Spanning tree
14. Union find (Disjoint sets)
15. Dynamic Programming
16. python libraries
17. <br>
<br>
<br>
Week 1:
In this week, I have worked on building the basic foundation of the python which includes building algorithms, understanding loops, Understanding conditional problems.<br>
<br>
The google colab link of week 1 assignment is given below:<br>
https://colab.research.google.com/drive/1MEr4SLyOVmL798kiUbK5KwfyODcLczBD?usp=sharing <br>
<br>
<br>
Week 2:
This week focuses on how to create set ?, dictionaries how to use algorithms like sorting and searching can be used to get the required information as output for
given input ? also under data structure of python more deeply. <br>
<br>
The google colab link of week 2 assignment is given below: <br>
https://colab.research.google.com/drive/1hK6JBI5VwNROKfD5DlxH2JfQEeSz-F-2?usp=sharing <br>
<br>
<br>
Week 3:
This week mainly focuses on learning recursion fundamentals and algorithms like Binary Search, merge  and merge & sort. it also includes building basics of greedy and backtracking and Time and space complexity.<br>
<br>
The google colab link of week 3 assignment is given below:<br>
https://colab.research.google.com/drive/1Y7YthVlEpJZdPqac3s0OuIJ--j2CEGLh?usp=sharing <br>
<br>
<br>
week 4:
This week focuses on learning the implementation of dijkastra's, kahn's and kosajaru's algorithm for solving questions of finding shortest path or maximizing output this week also focuses on building foundational knowledge on graph basics and implementation of techniques like BFS and DFS for graph traversal as well as
cycle detection.<br>
<br>
The google colab link of week 4 assignment is given below:<br>
https://colab.research.google.com/drive/1e0Hex861vLfEMflewH39xU3Jo2rg8Xs4?usp=sharing <br>
<br>
<br>
week 5:
This week focuses on learning the logic behind dynamic programming a powerful technique too solve problems by breaking them down into simpler subproblems. understanding difference between recursion, memoization
, and tabulation, tracing common pattern in DP problems and solving classic problems.<br>
<br>
The google colab link of week 5 assignment is given below:
https://colab.research.google.com/drive/1mrtljp-MK9x-AoU8F_wZ2u7QguIvknb4?usp=sharing<br>
<br>
<br>
week 6:
This week focuses on understanding implementation of python libraries, how to write shorter and cleaner code using the python libraries. Not just memorizing python functions but learning how yto find and use
them to built code with clean structure and good implementation<br>
<br>
The google colab link for week 6 assignment is given below:
https://colab.research.google.com/drive/1LwYBXfmc9gtcQRt1AJX68RJ6DsukDlyt?usp=sharing<br>
<br>
<br>
week 7:
This week focuses on building python contest strategies and managing time constraint along with the optimization of the problem output by performing code analysis with the focused contest mindset. in this week i have participated in code contests on platforms like codeforces and leet code to test my skills and knowledge<br>
<br>
<br>
week 8:
This week focuses on Building python project:
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
 Cell  Cost 
 S  -  0 
 E -  0 
 . -  1 
 T -  3 
 M -  5 
 # -  Blocked 
<br>
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

