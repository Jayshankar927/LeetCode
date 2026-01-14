'''
    Given an array nums of size n, return the majority element.

    The majority element is the element that appears more than ⌊n / 2⌋ times. 
    You may assume that the majority element always exists in the array.
'''
from collections import Counter

def majorityElement(self, nums: list[int]) -> int:
    C = Counter(nums)
    for key in C:
        if C[key] > len(nums) / 2:
            return int(key)