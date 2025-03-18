class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low = 0
        high = len(nums)-1
        lower = -1
        higher = -1

        while low<=high:
            mid = (low+high)//2
            if nums[mid]==target:
                lower = mid
                high = mid-1
            elif nums[mid]<target:
                low = mid+1
            else:
                high = mid-1
        
        low = 0
        high = len(nums)-1
        while low<=high:
            mid = (low+high)//2
            if nums[mid]==target:
                higher = mid
                low = mid+1
            elif nums[mid]>target:
                high = mid-1
            else:
                low = mid+1
        return (lower,higher)
        