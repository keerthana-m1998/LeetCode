class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = -1
        for i in range(len(nums)):
            if nums[i]==0: # find first zero element with its index
                j = i # assign it to j
                break
        if j==-1: # return if no zeros in array
            return
        for i in range(j+1,len(nums)): # i is next from j (2 pointer)
            if nums[i]!=0:
                nums[i],nums[j] = nums[j],nums[i]
                j+=1 # increment j after swapping
        
        