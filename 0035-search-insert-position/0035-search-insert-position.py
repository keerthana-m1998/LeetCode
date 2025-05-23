class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        ans = -1

        while low<=high:
            mid = (high+low)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                high = mid-1
            else:
                low = mid+1
        return high+1