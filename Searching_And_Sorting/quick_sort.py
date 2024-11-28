import  random

numbers = [int(x) for x in input().split()]


def quick_sort(nums):
    if len(nums) <= 1:
        return nums
    pivot = random.choice(nums)
    smaller = [x for x in nums if x < pivot]
    larger = [x for x in nums if x > pivot]
    equal = [x for x in nums if x == pivot]

    return quick_sort(smaller) + equal + quick_sort(larger)


print(*quick_sort(numbers))

