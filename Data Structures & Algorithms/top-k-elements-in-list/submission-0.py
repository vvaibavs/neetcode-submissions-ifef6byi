import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = [[] for k in range(len(nums)+1)]
        freq = {}
        for i in nums:
            freq[i] = freq.get(i, 0) + 1 
        
        for j, i in freq.items():
            count[i].append(j)

        res = []
        i = len(nums) - 1
        while k>0:
            for n in count[i]:
                res.append(n)
                k-=1
            i-=1
        return res

        
