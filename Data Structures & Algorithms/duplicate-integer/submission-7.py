class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        tempSet = set()
        for n in nums:
            if n in tempSet:
                return True
            else:
                tempSet.add(n)
        
        return False