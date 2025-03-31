class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r=0,1
        maxP = 0
        while r!=len(prices):
            if prices[l]<prices[r]:
                profit = (prices[r]-prices[l]) #minor conditions check for edge cases, be carefull with it
                maxP = max(maxP,profit)
            else:
                l =r
            r +=1
        return maxP