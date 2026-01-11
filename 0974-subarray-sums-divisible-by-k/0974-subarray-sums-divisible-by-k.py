class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix = defaultdict(int)
        prefix[0]=1
        curr_sum = 0
        result = 0

        for num in nums:
            curr_sum +=num
            remainder = curr_sum%k
            if remainder < 0:
                remainder+=k
            result+=prefix[remainder]
            prefix[remainder]+=1

        return result