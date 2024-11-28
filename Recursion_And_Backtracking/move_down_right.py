rows = int(input())  # m
cols = int(input())  # n

maze = []


for _ in range(rows):
    maze.append(["-"] * cols)


def find_paths(matrix, paths=0, row=0, col=0):
    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]):
        return paths

    if row == len(matrix) - 1 and col == len(matrix[0]) - 1:
        return paths + 1

    paths = find_paths(matrix, paths, row, col + 1)
    paths = find_paths(matrix, paths, row + 1, col)

    return paths


print(find_paths(maze))
