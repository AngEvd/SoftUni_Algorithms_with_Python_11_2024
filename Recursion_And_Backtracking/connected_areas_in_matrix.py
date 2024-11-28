rows = int(input())
cols = int(input())

matrix = []
areas = []

for _ in range(rows):
    matrix.append(list(input()))


def find_area(row, col, matrix, size=0):
    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]):
        return size
    if matrix[row][col] != "-":
        return size

    matrix[row][col] = "+"
    size += 1

    size = find_area(row - 1, col, matrix, size)
    size = find_area(row + 1, col, matrix, size)
    size = find_area(row, col - 1, matrix, size)
    size = find_area(row, col + 1, matrix, size)

    return size


for row in range(rows):
    for col in range(cols):
        size = find_area(row, col, matrix)
        if size == 0:
            continue
        areas.append((row, col, size))

sorted_areas = sorted(areas, key=lambda x: (-x[2], x[0], x[1]))
print(f"Total areas found: {len(sorted_areas)}")
for i in range(0, len(sorted_areas)):
    print(f"Area #{i + 1} at ({sorted_areas[i][0]}, {sorted_areas[i][1]}), size: {sorted_areas[i][2]}")
