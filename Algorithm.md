# Algorithm

## Step 1
Generate a random square maze containing:
- S -(Start)
- E -(End)
- . -(Empty Cell)
- T -(Trap)
- M - (Monster)
- #(Wall)

## Step 2
Assign traversal costs:

| Cell | Cost |
|------|------|
| S | 0 |
| E | 0 |
| . | 1 |
| T | 3 |
| M | 5 |
| # | Blocked |

## Step 3
Convert the maze into a graph.
Each traversable cell is treated as a graph node connected to its valid neighbouring cells.

## Step 4
Apply Dijkstra's Algorithm:
1. Initialize all node distances as infinity.
2. Set the start node distance to 0.
3. Use a priority queue to always process the node with the smallest distance.
4. Update neighbouring node distances whenever a shorter path is found.
5. Continue until the destination is reached.

## Step 5
Reconstruct the shortest path using parent pointers.

## Step 6
Display:
- Shortest Path
- Total Path Cost
- Number of Monsters Encountered
