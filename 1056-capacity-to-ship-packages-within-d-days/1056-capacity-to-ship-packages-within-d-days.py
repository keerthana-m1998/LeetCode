def cap(weights,cap1,days):
    total = 0
    cnt = 1
    n = len(weights)
    for i in range(n):
        if total+weights[i]>cap1:
            total = weights[i]
            cnt +=1
        else:
            total +=weights[i]
    return cnt
    
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        summ = 0 
        for i in weights:
            summ +=i
        high = summ
        while low<=high:
            mid = (low+high)//2
            ans = cap(weights,mid,days)
            if ans <= days:
                high = mid-1
            else:
                low = mid+1
        return low
        
        