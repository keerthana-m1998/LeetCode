class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        low,high = 0,n-1 # Binary search
        while low<=high:
            mid = (low+high)//2
            if nums[mid]==target:
                return mid
            # Left Sorted range
            if nums[low]<=nums[mid]: #checking for target and Eliminating 
                if nums[low]<=target<=nums[mid]: # Sorted part of arrays
                    high = mid-1
                else:
                    low = mid+1
            else: # Right Sorted range
                if nums[mid]<=target<=nums[high]:  # checking if target is present
                    low = mid+1
                else:
                    high = mid-1
        return -1

        