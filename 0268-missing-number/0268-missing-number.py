class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #SOLUTION:#1
        # nums.sort()
        # for i,value in enumerate(nums):
        #     # enumerate gives index and value at the same time
        #     if i != value:
        #         return i
        
        # if i == len(nums)-1:
        #    return value+1
        #     #Edge case:if value happens to be the last element of the list
        #     # ex : [0,2,1]

        #Solution :#2
        return sum(range(len(nums)+1))-sum(nums)
        #      range excludes last num, 
        #       ex: [0,2,1] len = 3 , sum(range(0,4))= 0+1+2+3
        #                   6 - 3 = 3 missing num
        