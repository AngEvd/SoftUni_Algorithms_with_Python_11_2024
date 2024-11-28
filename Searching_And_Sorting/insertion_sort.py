numbers = [int(x) for x in input().split()]


def insertion_sort(nums: list[int]):
    for i in range(len(nums)):
        j = i
        while j > 0 and nums[j] < nums[j - 1]:
            nums[j], nums[j - 1] = nums[j - 1], nums[j]
            j -= 1

    return f"{' '.join(map(str, nums))}"


print(insertion_sort(numbers))
