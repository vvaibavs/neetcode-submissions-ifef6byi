import heapq
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        difference = []
        for a in arr:
            difference.append((-abs(a-x), a))
        heap = difference[:k]
        heapq.heapify(heap)
        print(heap)
        for i in range(k, len(difference)):
            if difference[i][0] > heap[0][0]:
                heapq.heapreplace(heap, (difference[i][0], arr[i]))
            elif difference[i][0] == heap[0][0]:
                heapq.heapreplace(heap, (difference[i][0], min(difference[i][1], heap[0][1])))
        
        res = []
        for i in range(len(heap)):
            res.append(heap[i][1])

        return sorted(res)
