class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # O(N Log N) + O(N)
        # nums.sort()
        # count = 1
        # maxC = 1
        # if len(nums)==0:
        #     return 0
        # for i in range(1,len(nums)):
        #     if nums[i]-nums[i-1]==1:
        #         count+=1
        #         maxC = max(maxC,count)
        #     elif nums[i]==nums[i-1]:
        #         continue
        #     else:
        #         count = 1
        # return maxC

        # O(N) using sets
        numset = set(nums)
        longest = 0
        for n in numset:
            if (n-1) not in numset:
                length = 0
                while (n+length) in numset:
                    length +=1
                longest = max(length,longest)
        return longest
        