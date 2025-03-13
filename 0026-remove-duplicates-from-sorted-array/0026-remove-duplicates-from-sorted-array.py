class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # i = 0 
        # for j in range(1,len(nums)):
        #     if nums[i]!=nums[j]:
        #         nums[i+1]= nums[j]
        #         i+=1
        # return i+1  # i gives the unique elements of array

        # Hashset gives n(log N ) complexity
        # 2 pointer gives O(N)
        i = 0
        for j in range(1,len(nums)):
            if nums[i]!=nums[j]:
                nums[i+1]=nums[j]
                i+=1
        return i+1        