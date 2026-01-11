from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = defaultdict(int)
        seen[0]=1

        cur_sum = 0
        count = 0
        for num in nums:
            cur_sum+=num

            if cur_sum-k in seen:
                count+=seen[cur_sum-k]
            seen[cur_sum]+=1

        return count