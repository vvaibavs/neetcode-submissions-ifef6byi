class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = {}
        for n in range(0, len(nums)):
            if target - nums[n] not in temp:
                temp[nums[n]] = n
            else:
                return [temp.get(target-nums[n]), n]
        