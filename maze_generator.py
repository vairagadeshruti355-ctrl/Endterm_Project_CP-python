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
