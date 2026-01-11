class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        '''Prefix + Suffix Comparison
        Compute total sum first. For each index i, check if prefix_sum[i-1] == total - prefix_sum[i+1] '''
        
        summ = sum(nums)
        prefix = 0

        for i,num in enumerate(nums):
            if prefix == summ-prefix-num:
                return i
            prefix +=num

        return -1

#   Quick Dry Run

# For nums = [1, 7, 3, 6, 5, 6]:

# total = 28

# left_sum = 0

# Index 0, val = 1
# → left = 0
# → right = 28 - 0 - 1 = 27 → ❌

# left_sum = 1

# Index 1, val = 7
# → left = 1
# → right = 28 - 1 - 7 = 20 → ❌

# left_sum = 8

# Index 2, val = 3
# → left = 8
# → right = 28 - 8 - 3 = 17 → ❌

# left_sum = 11

# Index 3, val = 6
# → left = 11
# → right = 28 - 11 - 6 = 11 ✅ → return 3

# ⏱️ Complexity

# Time: O(n) – one pass

# Space: O(1) – just a few variables