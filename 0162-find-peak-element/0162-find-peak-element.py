class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        # Edge cases
        # 1
        if n == 1:
            return 0
        # 2 
        if nums[0]>nums[1]:
            return 0
        # 3 
        if nums[n-1]>nums[n-2]:
            return n-1
        low = 1
        high = n-1

        while low<=high:
            mid = (low+high)//2
            if nums[mid-1]<nums[mid]>nums[mid+1]:
                return mid
            # Rising array : peak is on right side
            # discard left
            if nums[mid-1]<nums[mid]:
                low = mid+1
            
            # decreasing array : peak is on left side
            # discard right
            else: 
                high = mid-1
        return -1

        