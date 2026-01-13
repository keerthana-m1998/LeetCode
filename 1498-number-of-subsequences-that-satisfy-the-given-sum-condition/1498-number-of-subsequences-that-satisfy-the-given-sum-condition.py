class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10**9 + 7
        nums.sort()  # CRITICAL: min=nums[left], max=nums[right]
        n = len(nums)
        
        # Precompute 2^0, 2^1, ..., 2^n (mod MOD)
        powers_of_two = [1] * (n + 1)
        for i in range(1, n + 1):
            powers_of_two[i] = (powers_of_two[i - 1] * 2) % MOD
        
        left, right = 0, n - 1
        result = 0
        
        while left <= right:
            # Check current min+max pair
            if nums[left] + nums[right] <= target:
                # All subsequences from left to right are valid!
                # Number of ways: 2^(right-left) combinations of middle elements
                result = (result + powers_of_two[right - left]) % MOD
                left += 1  # Try larger min (greedy: more restrictive)
            else:
                # Too large: shrink max
                right -= 1
        
        return result


            

