class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        temp = set()
        for n in nums:
            temp.add(n)
        
        if len(temp) != len(nums):
            return True
        return False