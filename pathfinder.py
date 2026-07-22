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
