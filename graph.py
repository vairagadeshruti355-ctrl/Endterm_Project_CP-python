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
