class Solution:
    """LeetCode 18: 4Sum - Sort + Two Nested Loops + Two Pointers
    
    EXTENSION OF 3Sum:
    3Sum: Fix i → left,right for nums[i]+nums[l]+nums[r]==0
    4Sum: Fix i,j → left,right for nums[i]+nums[j]+nums[l]+nums[r]==target
    
    Time Complexity: O(n³) - Two fixed loops O(n²) × Two pointers O(n)
    Space Complexity: O(1) - Output space excluded
"""
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort() # O(n log n) - Critical for duplicates & two pointers
        res = []
        n = len(nums)

            # Fix FIRST index (outermost loop)
        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:   # Skip duplicates for i
                continue
                
            # Fix SECOND index (nested loop)
            for j in range(i+1,n):
                if j>i+1 and nums[j]==nums[j-1]:    # Skip duplicates for j
                    continue

                # Two pointers for REMAINING pair
                left,right=j+1,n-1

                while left<right:
                    # Found valid quadruplet
                    total = nums[i]+nums[j]+nums[left]+nums[right]
                    if total==target:   # Found valid quadruplet
                        res.append([nums[i],nums[j],nums[left],nums[right]])

                        # Skip duplicates for left pointer
                        while left<right and nums[left]==nums[left+1]:
                            left+=1

                        # Skip duplicates for right pointer
                        while left<right and nums[right]==nums[right-1]:
                            right-=1
                        left+=1
                        right-=1

                    elif total<target:
                        left+=1     # Need larger sum

                    else:
                        right-=1    # Need smaller sum
        return res