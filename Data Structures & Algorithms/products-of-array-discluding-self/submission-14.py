class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        res = [1] * len(nums)
        left = 1
        for n in range(len(nums)):
            res[n] = left
            left *= nums[n]

        right = 1
        for n in range(len(nums)-1, -1, -1):
            res[n] *= right
            right *= nums[n]
        
        return res

