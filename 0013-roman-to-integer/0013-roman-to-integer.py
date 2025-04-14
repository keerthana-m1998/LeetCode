class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        ans = 0
        # for i,j in zip(s,s[1:]):
        #     if roman[i]<roman[j]:
        #         ans -=roman[i]
        #     else:
        #         ans+=roman[i]

        # return ans + roman[s[-1]]

# alternate
        n = len(s)
        for i in range(n):
            if i<n-1 and roman[s[i]]<roman[s[i+1]]:
                ans -= roman[s[i]]
            else:
                ans+= roman[s[i]]
        return ans
        