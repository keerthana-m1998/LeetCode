class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        # Mathematical solution
        power = 1
        ans = 0
        while sum(map(int,str(n))) > target:
            ans += power*(10-n%10)
            n = n//10 + 1
            power*=10
        return ans
        