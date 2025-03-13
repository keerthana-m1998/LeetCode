class Solution:
    def check(self, nums: List[int]) -> bool:
        # count = 0
        # for i in range(len(nums)): 
        #     if nums[i]>nums[(i+1)%len(nums)]: #mod helps with index out of range
        #         count +=1
        # return count<=1
        # in a rotated/non rotated array
        # nums[i] > nums[i+1] can occure only once
        # ex: [3,4,5,1,2], [2,1,3,4], [1,2,3]
        count = 0
        for i in range(len(nums)):
            if nums[i]>nums[(i+1)%len(nums)]:
                count+=1
        return count<=1