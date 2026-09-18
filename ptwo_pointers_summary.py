"""Two sum II"""
array = [1,2,3,4,5,6,7,8,9]
target = 8


class TwoSumII:
    left = 0
    right = len(array)-1

    while left < right:
        if array[left] + array[right] < target:
            left += 1
        elif array[left] + array[right] > target:
            right -= 1
        else:
            return [left + 1, right + 1]

    return []

