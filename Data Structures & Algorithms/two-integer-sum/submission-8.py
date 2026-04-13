class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tempMap = {}
        res = []
        for i in range(len(nums)):
            if target-nums[i] not in tempMap:
                tempMap[nums[i]] = i
            else:
                if i > tempMap.get(target-nums[i]):
                    return [tempMap.get(target-nums[i]), i]    
                return [i, tempMap.get(target-nums[i])]
                

            
                      
        