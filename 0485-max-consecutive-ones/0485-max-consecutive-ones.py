class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt = 0
        max_count = 0
        for num in nums:
            if num == 1:
                cnt+=1
                max_count = max(max_count,cnt)
            else:
                cnt = 0
        return max_count