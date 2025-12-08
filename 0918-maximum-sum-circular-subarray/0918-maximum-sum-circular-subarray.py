
    # """
    # Returns the maximum sum of a non-empty subarray of a circular array.
    # Intuition:
    # - Compute max subarray sum using Kadane (non-wrap case).
    # - Compute min subarray sum using Kadane on inverted logic.
    # - The wrap case (subarray that uses both end and start) equals:
    #     total_sum - min_subarray_sum.
    # - If all numbers are negative, max_subarray_sum will be the largest (least negative),
    #   and we must NOT use the wrap formula (which would yield 0).
    # """
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # Initialize Kadane states for max and min subarray
        cur_max = cur_min = nums[0]
        max_sum = min_sum = nums[0]
        total_sum = nums[0]

        for num in nums[1:]:
            # Kadane for maximum subarray sum
            total_sum+=num
            cur_max = max(cur_max+num, num)
            max_sum = max(cur_max,max_sum)

            # Kadane for minimum subarray sum
            cur_min = min(num,cur_min+num)
            min_sum = min(min_sum,cur_min)
        
    # If all numbers are negative, max_sum is the answer (no wrap)
    # Otherwise, take max of non-wrap and wrap cases

        if max_sum<0:
            return max_sum
        return (max(max_sum,(total_sum-min_sum)))




# 🔍 Dry Runs (Step-by-step)
# Example 1: nums = [5, -3, 5] → Expected output: 10 (wrap)

# total_sum = 5 + (-3) + 5 = 7
# Kadane max subarray:
# cur_max: 5 → max( -3, 5-3=2 )→ 2 → max( 5, 2+5=7 )→ 7
# max_sum = 7

# Kadane min subarray:
# cur_min: 5 → min( -3, 5-3=2 )→ -3 → min( 5, -3+5=2 )→ -3
# min_sum = -3

# Wrap case: total_sum - min_sum = 7 - (-3) = 10
# Answer: max(7, 10) = 10

# This corresponds to taking the wrap-around subarray [5, 5] (i.e., index 0 and index 2), which sums to 10.



# Example 2: nums = [-3, -2, -3] → Expected output: -2 (no wrap)

# total_sum = -8
# Kadane max subarray:
# Progressive best stays at -2 (largest element)
# Kadane min subarray = -8 (the whole array)
# Since max_sum <= 0, we return max_sum = -2 (no wrapping allowed).
        