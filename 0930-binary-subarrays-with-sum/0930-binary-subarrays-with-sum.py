class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix = defaultdict(int)
        prefix[0] = 1
        curr_sum = 0
        count = 0

        for num in nums:
            curr_sum +=num
            
            count+=prefix[curr_sum-goal]
            prefix[curr_sum]+=1

        return count   