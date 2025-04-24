class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        max_reach = 0
        for i in range(n):
            if max_reach <i:
                return False
            max_reach = max(max_reach,nums[i]+i)
            if max_reach >= n-1:
                return True
        return True