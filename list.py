#!/usr/bin/python3
def numbers(nums,target):

    for i in range(len(nums)):
        for j in range(len(nums)):
            if i == j :
                continue
            elif nums[i] + nums[j] == target:
                return (i,j)

