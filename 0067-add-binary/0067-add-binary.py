class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i ,j = len(a)-1,len(b)-1
        res = []
        carry = 0 
        while i>=0 or j>=0 or carry:
            a_bit = a[i] if i>=0 else 0         # ex : 1010, 10
            b_bit = b[j] if j>=0 else 0  # Edge case for un Even digits
            summ = carry + int(a_bit) + int(b_bit)
            carry = summ//2
            res.append(str(summ%2))

            i-=1
            j-=1
        return ''.join(reversed(res))

        