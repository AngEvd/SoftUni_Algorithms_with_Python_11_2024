def recursive_drawing(n: int):
    if n <= 0:
        return
    print("*" * n)
    recursive_drawing(n - 1)
    print("#" * n)


recursive_drawing(int(input()))