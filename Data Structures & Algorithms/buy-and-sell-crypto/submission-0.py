class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b = 0
        s = 1
        maxP = 0
        while b < len(prices) and s < len(prices):
            if prices[b] > prices[s]:
                b = s
            elif prices[s] > prices[b]:
                tempP = prices[s] - prices[b]
                if tempP > maxP:
                    maxP = tempP
                s+=1
            else:
                s+=1
        return maxP

