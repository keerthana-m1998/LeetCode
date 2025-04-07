class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # NEETCODE
        total = len(nums1)+len(nums2) # FInd total len
        half = total//2     # go through bigger examples
        A,B = nums1,nums2
        if len(B)<len(A):   # Binary search on shorter array
            A,B = B,A
        
        l,r =0,len(A)-1     # shorter array low and high
        while True:         # median if confirmed to br found i,e. True
            i = (l+r)//2    # mid for A
            j = half-i-2    # mid for B (since i is also a part of half)
            Aleft = A[i] if i>=0 else float('-inf') # mid (left) of A if array goes out of bound ##Edge case 
            Aright = A[i+1] if (i+1)<len(A) else float('inf') # mid+1 of A (right) 
            Bleft = B[j] if j>=0 else float('-inf') # mid (left) of B
            Bright = B[j+1] if (j+1)<len(B) else float('inf')   # mid+1 of B (right)

            if Aleft<=Bright and Bleft<=Aright: # Check if symmetric array partition is done
                # If total array is Odd
                if total%2:
                    return min(Aright,Bright)
                # If total array is Even
                return (min(Aright,Bright)+max(Aleft,Bleft))/2
            # A has more elements, move high/r to mid-1 to move elements to left
            elif Aleft>Bright:
                r = i-1
           # A has less elements, move low/l to mid+1 to move elements to right
            else:
                l = i+1
        # Striver Code
        # n1,n2 = len(nums1),len(nums2)
        # if n1>n2:
        #     self.findMedianSortedArrays(nums2,nums1)
        # n = n1+n2
        # left = (n1+n2+1)//2

        # low,high = 0,n1
        # while low<=high:
        #     mid1 = (low+high)//2
        #     mid2 = left-mid1
        #     l1,l2,r1,r2= float('-inf'),float('-inf'),float('inf'),float('inf')
        #     if mid1 < n1:
        #         r1 = nums1[mid1]
        #     if mid2 < n2:
        #         r2 = nums2[mid2]
        #     if mid1-1 >= 0:
        #         l1 = nums1[mid1-1]
        #     if mid2-1 >= 0:
        #         l2 = nums2[mid2-1]
            
        #     if l1 <= r2 and l2 <= r1:
        #         if n%2==1:
        #             return max(l1,l2)
        #         else:
        #             # maxi=float(max(l1,l2)
        #             # minV=float(min(r1,r2)
        #             # return maxi+minV)/2.0

        #             return (float(max(l1,l2))+float(min(r1,r2)))/2.0
        #     elif l1>r2:
        #         high = mid1-1
        #     else:
        #         low = mid1+1
        # return 0

        