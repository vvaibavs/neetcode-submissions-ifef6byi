class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b = 0 
        s = 1
        m = 0
        while b < len(prices) and s < len(prices):
            if prices[s] < prices[b]:
                b = s
                s+=1
            else:
                m = max(m, prices[s] - prices[b])
                s+=1
        return m 