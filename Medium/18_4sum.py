'''Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

 

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]'''

def foursum(nums, target):
    def findNsum(nums, start, target, N, path, res):
        # Early termination
        if N < 2 or len(nums) - start < N:
            return
        if target < nums[start] * N or target > nums[-1] * N:
            return

        # Base case: 2-sum
        if N == 2:
            l, r = start, len(nums) - 1
            while l < r:
                s = nums[l] + nums[r]
                if s == target:
                    res.append(path + [nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif s < target:
                    l += 1
                else:
                    r -= 1
            return

        # Recursive case
        for i in range(start, len(nums) - N + 1):
            if i > start and nums[i] == nums[i - 1]:
                continue
            findNsum(nums, i + 1, target - nums[i], N - 1, path + [nums[i]], res)


    
    nums.sort()

    res = []
    findNsum(nums, 0, target, 4, [], res)
    print(res)
