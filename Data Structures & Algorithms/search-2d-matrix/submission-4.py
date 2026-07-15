class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        res = []
        for n in matrix:
            for m in n:
                res.append(m)
        if target == res[0]:
            return True
        while len(res) > 1:
            if target > res[int(len(res)/2)]:
                res = res[int(len(res)/2):]
            elif target < res[int(len(res)/2)]:
                res = res[:int(len(res)/2)]
            else:
                return True
        return False
        