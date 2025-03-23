class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """Do not return anything, modify nums in-place instead."""
        # cnt1=0
        # cnt2=0   #counter variable , keeping track of occurences
        # cnt0 = 0
        # for num in nums:
        #     if num==0:
        #         cnt0+=1
        #     elif num==1:
        #         cnt1+=1
        #     else:
        #         num==2
        #         cnt2+=1
        # for i in range(0,cnt0):
        #     nums[i] = 0 
        # for i in range(cnt0,cnt0+cnt1):
        #     nums[i]=1
        # for i in range(cnt0+cnt1,len(nums)):
        #     nums[i]=2


#Dutch National Flag algorithm
        low,mid = 0,0
        high = len(nums)-1
        while(mid<=high):
            if nums[mid]==0:
                nums[mid],nums[low]=nums[low],nums[mid]
                mid+=1
                low+=1
            elif nums[mid]==1:
                mid+=1
            else:
                nums[mid],nums[high]=nums[high],nums[mid]
                high-=1
                