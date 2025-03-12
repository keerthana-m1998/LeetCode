class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # Compare elements from last and append to nums1
        last = m+n-1 # last indx of nums1 is m+n (m-> length of nonzero elements)
        # [1,2,3,0,0,0] [2,5,6]
        # m = 3 nums1[m-1]=3 (last element comparision)
        # n = 3 nums2[n-1]=6 
        # nums1[last]= 0
        while m>0 and n>0:
            if nums1[m-1]>nums2[n-1]:
                nums1[last]=nums1[m-1]
                m-=1
            else:
                nums1[last]=nums2[n-1]
                n-=1
            last-=1

# Edge case 1: for elements remaining in nums2
        while n>0: 
            nums1[last]=nums2[n-1]
            last,n = last-1,n-1
        
        