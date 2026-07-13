class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maximum = 0
        for n in nums:
            if n:
                count+=1
            else:
                if count > maximum:
                    maximum = count
                count = 0
        if count > maximum:
            maximum = count
            count = 0
        return maximum