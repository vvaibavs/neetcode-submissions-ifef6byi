class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix = 0
        remainders = {}

        for i, n in enumerate(nums):
            prefix += n
            if prefix % k == 0 and i >= 1:
                return True
            elif prefix % k in remainders:
                if i - remainders[prefix%k] >=2:
                    return True  
            elif prefix % k not in remainders:
                remainders[prefix%k] = i
        return False
