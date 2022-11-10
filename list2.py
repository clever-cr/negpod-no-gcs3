#!/usr/bin/python3
def numbers(nums, target):

    sorted_list = sorted(nums)
    if target in sorted_list:
        return sorted_list.index(target)
    else:
        pass


result = numbers([1, 3, 5, 6], 7)
print(result)
