array = [int(x) for x in input().split()]


def array_sum(numbers: list):
    if len(numbers) == 1:
        return numbers[0]
    return numbers[-1] + array_sum(numbers[:-1])


print(array_sum(array))




