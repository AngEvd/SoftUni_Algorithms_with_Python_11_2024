rows = int(input())
cols = int(input())

maze = []

for _ in range(rows):
    maze.append(list(input()))


def find_all_paths(row, col, matrix, direction, path):
    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]):
        return

    if maze[row][col] == "*":
        return
    if maze[row][col] == "v":
        return

    path.append(direction)

    if maze[row][col] == "e":
        print(''.join(path))

    else:
        maze[row][col] = "v"

        find_all_paths(row, col - 1, matrix, "L", path)
        find_all_paths(row, col + 1, matrix, "R", path)
        find_all_paths(row - 1, col, matrix, "U", path)
        find_all_paths(row + 1, col, matrix, "D", path)

        maze[row][col] = "-"

    path.pop()



find_all_paths(0, 0, maze, "", [])
