class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = 2**31-1
        INT_MIN = -2**31
        i = 0
        num = 0
        n = len(s)
        sign = 1
        # Skip white spaces
        while i<n and s[i]==" ":
            i+=1

        # Handle sign 
        if i<n and s[i] in "+-":
            sign = -1 if s[i]=='-' else 1
            i+=1

        # Parse digits 
        while i<n and s[i].isdigit():
            digit = int(s[i])
            # CHeck overflow
            if num > (INT_MAX-digit)//10:
                return INT_MAX if sign == 1 else INT_MIN
            num = num*10+digit
            i+=1

        return max(INT_MIN,min(sign*num,INT_MAX))
        