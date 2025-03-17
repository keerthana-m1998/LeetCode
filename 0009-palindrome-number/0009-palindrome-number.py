class Solution:
    def isPalindrome(self, x: int) -> bool:
        # -ve nums are not palindromes 
        if x<0:
            return False
# reversing string == X ?
        else:
            return True if int(str(x)[::-1]) == x else False

        # RPGRM 17-03-2025
        # if x<0:
        #     return False
        # else:
        #     return True if int(str(x)[::-1])==x else False
        