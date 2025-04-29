class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        nums = []
        forbidden = set()
        i = 1
        while len(nums)<n:
            if i not in forbidden:
                nums.append(i)
                forbidden.add(k-i)
            i+=1
        return sum(nums)
        