class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hp = {}
        for i in range (len(nums)):
            remainder = target - nums[i]
            if remainder in hp:
                return [hp[remainder], i]
            hp[nums[i]] = i
        
        return 1

            
            
