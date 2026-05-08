class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = {}
        for i in range(len(nums)):
            remainder = target - nums[i]
            print(remainder)
            if remainder not in temp:
                temp[nums[i]] = i
            else:
                return [temp.get(remainder), i]
                

            
                      
        