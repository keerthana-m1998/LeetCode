def possibleSplit(arr,rangeSum):
    n = len(arr)
    cnt = 1
    summ = 0
    for i in range(n):
        if summ+arr[i]<=rangeSum:
            summ+=arr[i]
        else:
            cnt+=1
            summ = arr[i]
    return cnt

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n<k:
            return -1
        low = max(nums)
        high = sum(nums)
        while low<=high:
            mid = (low+high)//2
            ans = possibleSplit(nums,mid)
            if ans > k :
                low = mid+1
            else:
                high = mid-1
        return low
        