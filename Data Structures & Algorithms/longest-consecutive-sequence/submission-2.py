class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        total = 0
        consec = 1
        found = False
        for n in hashset:
            if n - 1 not in hashset:
                current = n
                while current + 1 in hashset:
                    consec += 1
                    current = current + 1
                total = max(total, consec)
                consec = 1
        
        return total



        