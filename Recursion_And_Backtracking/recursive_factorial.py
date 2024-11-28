def recursive_factorial(n: int):
    if n == 0:
        return 1
    else:
        return n * recursive_factorial(n - 1)


print(recursive_factorial(int(input())))

