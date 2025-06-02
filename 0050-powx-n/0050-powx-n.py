class Solution:
    def myPow(self, x: float, n: int) -> float:
        # divide and conqure using recursion
        # 2^10 = 2^5 * 2^5  # Even N Val
        # 2^5 = 2 * 2^2 * 2^2 # Odd N Val
        # 2^-2 = 1/2*2 # -ve Val
        def recurse(x,n):
            if x == 0: return 0
            if n == 0: return 1
            res = recurse(x,n//2)
            res = res*res
            return x*res if n%2 else res

        res = recurse(x,abs(n))
        return res if n>=0 else 1/res # for -ve val 
        