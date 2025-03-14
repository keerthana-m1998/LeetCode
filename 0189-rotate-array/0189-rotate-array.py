class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # rotate whole array ( by swapping, (0 --> n-1))
        k = k%len(nums)
        l = 0
        r = len(nums)-1
        while l<r:
            nums[l],nums[r]= nums[r],nums[l]
            l+=1
            r-=1
        # rotate array by parts of K (0 --> k-1)
        l,r = 0,k-1
        while l<r:
            nums[l],nums[r]=nums[r],nums[l]
            l+=1
            r-=1
        # rotate array by parts of K (k --> n-1)
        l,r =k,len(nums)-1
        while l<r:
            nums[l],nums[r]=nums[r],nums[l]
            l+=1
            r-=1