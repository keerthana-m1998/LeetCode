class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        
        # Try all possible x from 1 to n
        for x in range(1, n + 1):
            # index of the first element among the last x elements
            idx = n - x
            
            # Check if there are at least x elements >= x
            if nums[idx] >= x:
                # If there is an element before idx, it must be < x
                if idx == 0 or nums[idx - 1] < x:
                    return x
        
        return -1