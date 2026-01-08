'''Given two arrays nums1 and nums2.

Return the maximum dot product between non-empty subsequences of nums1 and nums2 with the same length.

A subsequence of a array is a new array which is formed from the original array by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, [2,3,5] is a subsequence of [1,2,3,4,5] while [1,5,3] is not).'''


def maxDotProduct(nums1,nums2):
    m,n = len(nums1), len(nums2)
    NEG = -10**25

    dp = [[NEG]*(n+1) for _ in range(m+1)]

    for i in range(m-1,-1,-1):
        for j in range(n-1,-1,-1):

            dp[i][j] = max(
                nums1[i] * nums2[j] + max(0,dp[i+1][j+1]),
                dp[i+1][j],
                dp[i][j+1]
            )

    return dp[0][0]

nums1 = [2,1,-2,5]
nums2 = [3,0,-6] #Output: 18
print(maxDotProduct(nums1,nums2))