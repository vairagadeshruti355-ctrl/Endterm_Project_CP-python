from maze_generator import generate_maze
from graph import create_graph
from pathfinder import shortest_path

maze = generate_maze()

print("Maze\n")

for row in maze:
    print(row)

graph = create_graph(maze)

path,cost,monsters = shortest_path(graph,maze)

print("\nShortest Path")

for node in path:
    print(node)

path, total_cost, monsters = shortest_path(graph, maze)

print("\nShortest Path:", path)
print("Total Path Cost:", total_cost)
print("Monsters Encountered:", monsters)
