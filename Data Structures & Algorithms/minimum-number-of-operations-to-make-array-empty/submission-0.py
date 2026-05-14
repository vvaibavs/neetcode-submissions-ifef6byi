class Solution:
    def minOperations(self, nums: List[int]) -> int:
        freq = {}
        count = 0
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        
        for n in freq:
            if freq[n] == 1:
                return -1
            while freq[n] - 3 >= 0:
                count += 1
                freq[n] -= 3
                print(n, freq[n])
            if freq[n] != 0:
                freq[n] += 3
                print(n, freq[n])
                count-=1
            while freq[n] - 2 >= 0:
                count += 1
                freq[n] -= 2
                print(n, freq[n])

        return count