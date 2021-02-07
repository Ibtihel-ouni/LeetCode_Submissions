class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        l = [1] * len(nums)
        
        for i in range(1,len(l)):
            subprobs = [l[k] for k in range(i) if nums[k] < nums[i] ]
            l[i] = 1 + max(subprobs , default = 0)
            
        return max(l , default = 0)
