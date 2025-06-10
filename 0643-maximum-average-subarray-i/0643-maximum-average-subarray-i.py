class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxx = float(-inf)
        i,j = 0,0
        summ = nums[i]
        if len(nums)==1:
            return summ
        while (j<len(nums)-1 and i<len(nums)-1):
            if (j-i+1)<k:
                j+=1
                summ+=nums[j]
                
            if (j-i+1)==k:
                avg = summ/k
                maxx = max(maxx,avg)
                summ -=nums[i]
                i+=1
        return maxx