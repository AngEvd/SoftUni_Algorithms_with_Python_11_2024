numbers = [int(x) for x in input().split()]


def merge(left, right):
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result.extend(left)
    result.extend(right)
    return result


def merge_sort(nums: list[int]) -> list:
    if len(nums) <= 1:
        return nums
    mid_idx = len(nums) // 2
    left = merge_sort(nums[:mid_idx])
    right = merge_sort(nums[mid_idx:])

    return merge(left, right)


print(*merge_sort(numbers))
