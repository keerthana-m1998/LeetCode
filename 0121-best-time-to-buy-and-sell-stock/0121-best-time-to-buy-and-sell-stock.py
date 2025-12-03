class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Sliding Windwo
        # l,r=0,1
        # maxP = 0
        # while r!=len(prices):
        #     if prices[l]<prices[r]:
        #         profit = (prices[r]-prices[l]) #minor conditions check for edge cases, be carefull with it
        #         maxP = max(maxP,profit)
        #     else:
        #         l =r # left cannot cross as buy day is before sell day
                        # left stops at minimum value
        #     r +=1     # right keeps moving to find maximum value
        # return maxP

        # 2nd approach 09-04-2025
        # min_price = float('inf')
        # max_p = 0
        # for price in prices:
        #     min_price = min(price,min_price)
        #     profit = price-min_price
        #     max_p = max(profit,max_p)
        # return max_p

        # Min-Max
        minV = float('inf')
        maxP = 0
        for i in prices:
            minV = min(minV,i)
            profit = i-minV
            maxP = max(maxP,profit)
        return maxP

