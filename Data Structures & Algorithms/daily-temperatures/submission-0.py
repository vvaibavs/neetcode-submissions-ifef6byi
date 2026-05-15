class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        for i, t in enumerate(temperatures):
            n = i
            while n<len(temperatures) and t >= temperatures[n]:
                n+=1
            if n < len(temperatures) and t < temperatures[n]:
                res.append(n-i)
            else:
                res.append(0)
        return res