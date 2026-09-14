class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hasmap = {}
        for n in range(len(nums)):
            if target - nums[n] not in hasmap:
                hasmap[nums[n]] = n
            else:
                return [hasmap[target-nums[n]], n]