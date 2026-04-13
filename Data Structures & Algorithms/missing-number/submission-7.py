class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        for i in range(len(nums)):
            if(i != nums[i]):
                return i
            if(i == len(nums) - 1 and nums[i] != len(nums)):
                return len(nums)
            
        return 0