class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        s = s.rstrip()
        for char in s:
            if char!=' ':
                count+=1
            else:
                count = 0
        return count