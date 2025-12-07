class Solution:
    def specialArray(self, nums: List[int]) -> int:
        n = len(nums)
        freq = [0]*(n+1) 
        # freq[i] = how many nums are exactly i (for i in [0, n])
        
        # any num > n is counted in freq[n]
        for num in nums:
            if num>=n:
                freq[n]+=1
            else:
                freq[num]+=1  # num and freq[num] are same
         # count_ge will track how many numbers are >= current x
        counter = 0


        # Try x from n down to 1
        for x in range(n,0,-1):
            counter += freq[x] # add numbers that are exactly x
            if counter == x:
                return x

        return -1


# nums = [0, 4, 3, 0, 4]
# n = 5

# Build freq:

# nums: 0,4,3,0,4

# freq[0] = 2
# freq[3] = 1
# freq[4] = 2
# others 0

# Now check from x = 5 → 1:

# x = 5: count_ge += freq[5] = 0 → count_ge = 0 ≠ 5
# x = 4: count_ge += freq[4] = 2 → count_ge = 2 ≠ 4
# x = 3: count_ge += freq[3] = 1 → count_ge = 3 ✅ count_ge == x → return 3
# And indeed in nums, elements ≥ 3 are: [4,3,4] → 3 elements → x = 3 ✅

# O(n),O(n)