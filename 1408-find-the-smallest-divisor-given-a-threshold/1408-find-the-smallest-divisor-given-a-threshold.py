def limitCalc(arr,test):
    summ = 0
    for a in arr:
        summ += ceil(a/test)
    return summ
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low = 1
        high = max(nums)
        while(low<=high):
            mid = (low+high)//2
            if limitCalc(nums,mid)<=threshold:
                high = mid-1
            else:
                low = mid+1
        return low
        