class Solution:
    def mySqrt(self, x: int) -> int:
        if x <2:
            return x
        # Binary search
        l,r = 0,x
        while l<=r:
            mid = l + (r-l) // 2
            if mid*mid == x:
                return mid
            elif mid*mid<x:
                l = mid+1
            else:
                r = mid-1
        return r

        