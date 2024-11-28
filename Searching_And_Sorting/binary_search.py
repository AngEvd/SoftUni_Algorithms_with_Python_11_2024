numbers = sorted([int(x) for x in input().split()])
target = int(input())


def binary_search(array: list, n: int):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid_idx = (left + right) // 2
        mid_num = array[mid_idx]

        if mid_num == n:
            return mid_idx
        elif mid_num < n:
            left = mid_idx + 1
        else:
            right = mid_idx - 1
    return -1


print(binary_search(numbers, target))