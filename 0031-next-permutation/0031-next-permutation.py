class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        #Do not return anything, modify nums in-place instead.
        indx = -1
        for i in range(len(nums)-2,-1,-1): #Find the break point
            if nums[i]<nums[i+1]:
                indx = i
                break
        if indx == -1:  # if no break point found, return the first permuation
            nums.reverse()
            return nums

        for i in range(len(nums)-1,indx,-1): #Swap brk point with first large num
            if nums[i]>nums[indx]:
                nums[i],nums[indx]=nums[indx],nums[i]
                break
        nums[indx+1:] = reversed(nums[indx+1:]) #return array with reveresed fron brk point to end
