class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        max_sum = 0
        left,right = 0,len(nums)-1
        while left<right:
            summ = nums[left]+nums[right]
            max_sum = max(summ,max_sum)
            left+=1
            right-=1
        return max_sum