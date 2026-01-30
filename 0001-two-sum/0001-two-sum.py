class Solution:
    '''
    check whether "target - x" already exists

    Time: O(n²) → nested loops
    Space: O(1) → no extra space
    '''
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Dictionary to store number -> index
        seen = {}
        # Iterate through the array
        for i in range(len(nums)):
            current = nums[i]
            
            # Check if the complement is already seen
            remaining = target-current
            # If yes, return indices
            if remaining in seen:
                return [seen[remaining],i]
            
            # Otherwise, store current number with its index
            seen[current]=i
