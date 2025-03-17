class Solution:
    def reverse(self, x: int) -> int:

        # # reverse string for both +ve and -ve 
        # # -ve num is reversed from indx 1 (- sign is at 0th indx)
        res = int(str(x)[::-1]) if x>=0 else -int(str(x)[1:][::-1])
        
        # # calculated res is checked for 32-bit range
        return res if res>-2**31 and res<2**31-1 else 0
        

        # Reprogram on 17-03-2025
        # res = int(str(x)[::-1]) if x>=0 else -int(str(x)[1:][::-1])
        # return res if res>-2**31 and res<2**31-1 else 0