'''Given an array nums, you can perform the following operation any number of times:

Select the adjacent pair with the minimum sum in nums. If multiple such pairs exist, choose the leftmost one.
Replace the pair with their sum.
Return the minimum number of operations needed to make the array non-decreasing.

An array is said to be non-decreasing if each element is greater than or equal to its previous element (if it exists).

 

Example 1:

Input: nums = [5,2,3,1]

Output: 2

Explanation:

The pair (3,1) has the minimum sum of 4. After replacement, nums = [5,2,4].
The pair (2,4) has the minimum sum of 6. After replacement, nums = [5,6].
The array nums became non-decreasing in two operations.

Example 2:

Input: nums = [1,2,2]

Output: 0

Explanation:

The array nums is already sorted.'''
import math

def minimumPairRemoval(nums):
    c=0
    i=0
    n=len(nums)
    while i<n-1:
        if(nums[i]>nums[i+1]):
            mini=math.inf
            index=0
            for j in range(n-1):
                if(mini>(nums[j]+nums[j+1])):
                    mini=nums[j]+nums[j+1]
                    index=j
            nums[index]=mini
            nums.pop(index+1)
            c=c+1
            n=n-1
            i=0
        else:
            i=i+1
    return c