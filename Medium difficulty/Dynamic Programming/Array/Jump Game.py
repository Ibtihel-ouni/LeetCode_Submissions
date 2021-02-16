class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n
        dp[0] = True
        right = 0
        
        for i in range(n):
            if dp[i]:
                for j in range(right, min(n-1,i+nums[i]) + 1):
                    dp[j] = True
                    right = j
        return dp[n-1]
