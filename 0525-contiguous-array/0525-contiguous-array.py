class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        seen = {0:-1}
        cur_sum = 0
        max_len = 0
        for i , num in enumerate(nums):
            cur_sum +=1 if num==1 else -1
            if cur_sum in seen:
                max_len = max(max_len,i-seen[cur_sum])
            else:
                seen[cur_sum]=i
        return max_len
        