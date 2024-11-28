n = int(input())
vector = [0] * n


def gen01(array: list, idx: int = 0):
    if idx >= len(array):
        print(f"".join(map(str, array)))
        return
    for num in range(2):
        array[idx] = num
        gen01(array, idx + 1)


gen01(vector)
