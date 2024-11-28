array = input().split()


def reverse_array(arr: list):
    if len(arr) == 0:
        return ""
    return arr[-1] + " " + reverse_array(arr[:-1])

print(reverse_array(array))
