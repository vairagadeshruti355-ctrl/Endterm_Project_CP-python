import random

cells = [".", ".", ".", "#", "T", "M"]

def generate_maze():
    cols = random.randint(3, 10)
    maze = []

    for i in range(cols):
        if i == 0:
            row = "S" + "".join(random.choice(cells) for _ in range(cols - 1))

        elif i == cols - 1:
            row = "".join(random.choice(cells) for _ in range(cols - 1)) + "E"

        else:
            row = "".join(random.choice(cells) for _ in range(cols))

        maze.append(row)

    return maze

def create_graph(maze):

    graph = {}

    cost = {
        'S':0,
        'E':0,
        '.':1,
        'T':3,
        'M':5,
        '#':8
    }

    directions = [
        (1,0),
        (-1,0),
        (0,1),
        (0,-1)
    ]

    n = len(maze)

    for i in range(n):
        for j in range(n):

            if maze[i][j] == '#':
                continue

            graph[(i,j)] = []

            for dr,dc in directions:

                nr = i + dr
                nc = j + dc

                if 0 <= nr < n and 0 <= nc < n:

                    if maze[nr][nc] != '#':

                        graph[(i,j)].append(
                            ((nr,nc),cost[maze[nr][nc]])
                        )

    return graph

import heapq

def shortest_path(graph, maze):

    start = None
    end = None

    n = len(maze)

    for i in range(n):
        for j in range(n):

            if maze[i][j]=='S':
                start=(i,j)

            elif maze[i][j]=='E':
                end=(i,j)

    dist = {node: float('inf') for node in graph}
    parent = {}

    dist[start] = 0

    pq = [(0,start)]

    while pq:

        current_cost,current = heapq.heappop(pq)

        if current==end:
            break

        for neighbour,weight in graph[current]:

            new_cost = current_cost + weight

            if new_cost < dist[neighbour]:

                dist[neighbour] = new_cost
                parent[neighbour] = current

                heapq.heappush(
                    pq,
                    (new_cost,neighbour)
                )

    path=[]

    node=end

    while node!=start:

        path.append(node)
        node=parent[node]

    path.append(start)

    path.reverse()

    monsters = sum(
        maze[r][c]=='M'
        for r,c in path
    )

    return path, dist[end], monsters

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
