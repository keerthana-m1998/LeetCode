class Solution:
    def fib(self, n: int) -> int:
        n0,n1 = 0,1
        if n ==0:
            return 0
        elif n ==1:
            return n0+n1
        else:
            for i in range (2,n+1): #6
                n2 = n1+n0     # n2 = 1,2,3,5,8
                summ = n2      # summ = 1,2,3,5
                n0 = n1     # n0 = 1,1,2,3
                n1 = n2     #n1 = 1,2,3,5
        return summ  