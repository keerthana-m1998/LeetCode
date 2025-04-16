class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        #Greedy Algorithm 
        #Track max_reachable value, coin>max_reach+1, break in sequence
        #Otherwise keep adding coing to max_reachable answer
        coins.sort()
        ans = 0
        for coin in coins:
            if coin>ans+1:
                break
            ans+=coin
        return ans+1