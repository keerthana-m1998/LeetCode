def possible(arr,day,k):
    # how many bouquets are possible for a given bloom day ( EX: 7)
    n = len(arr)
    cnt = 0
    no_of_B = 0
    for i in range(n):
        if arr[i]<=day: # Consecutive bloom count
            cnt +=1
        else:
            cnt = 0                # reset cnt (consecutive bloom count)
        if cnt == k:
            no_of_B += 1        # increase no. of bouquets cnt
            cnt = 0

    return no_of_B       # return true if ans == m (no of bouquets)  (TC:O(N))
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        # Impossible case
        val = m*k
        n = len(bloomDay)
        if n<val:
            return -1
        # Find Mini & Maxi range for B.S
        mini = float('inf')
        maxi = float('-inf')
        for i in range(n):
            maxi = max(maxi,bloomDay[i])
            mini = min(mini,bloomDay[i])

        # Binary Search
        low = mini
        high = maxi
        # ans = -1
        while low<=high:
            mid = (low+high)//2
            if possible(bloomDay,mid,k)>=m: # Check if m bouquets are possible
                # ans = mid
                high = mid-1        # move left to find minimum possible answer
            else:
                low = mid+1         # move right to find answer as its lower than M value
        return low                # at the end low will be pointing to answer
        