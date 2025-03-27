def findMax(piles):
    # Calculate the maximum possible answer(K) or range to run the Binary search
    # n = len(piles)
    maxi = float('-inf')
    for i in piles:
        maxi = max(i,maxi)
    return maxi
def calculateHours(piles,hourlyK):
    # Calculate Total hours for possible K values (total hours = total Bananas//no. of bananas per hour (K))
    Total_Hours = 0 
    n = len(piles)
    for i in range(n):
        Total_Hours += ceil(piles[i]/hourlyK)
    return Total_Hours


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = findMax(piles)
    # Binary Search to calculate minimum K value
        while low<=high:
            mid = (low+high)//2
            THours = calculateHours(piles,mid)
            if THours<=h: # if hours for K < h ( hours given)
                high = mid-1 # move left further to find minimum value of k
            else:
                low = mid+1  # move right to match given 'h' hours
        return low

        