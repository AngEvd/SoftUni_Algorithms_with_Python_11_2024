numbers = [int(x) for x in input().split()]


def bubble_sort(nums: list[int]):
    is_sorted = False
    i = 0
    while not is_sorted:
        is_sorted = True
        for j in range(1, len(nums) - i):
            if nums[j - 1] > nums[j]:
                nums[j - 1], nums[j] = nums[j], nums[j - 1]
                is_sorted = False
        i += 1

    return f"{' '.join(map(str, nums))}"


print(bubble_sort(numbers))
