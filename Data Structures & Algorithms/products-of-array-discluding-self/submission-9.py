class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        res = []
        for n in range(len(nums)):
            for i in range(n+1, len(nums)):
                prefix[n] *= nums[i]

        for n in range(len(nums)-1, -1, -1):
            for i in range(n-1, -1, -1):
                suffix[n] *= nums[i]

        for n in range(len(prefix)):
            res.append(prefix[n] * suffix[n])
        
        return res

