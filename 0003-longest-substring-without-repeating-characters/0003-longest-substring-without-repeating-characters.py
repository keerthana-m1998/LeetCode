class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Using Slidingg window ( maintain it as not to conatin any duplicates)
        # by using SET or DICTIONARY to keep track of duplicate CHARS
        l = 0
        res = 0
        CharSeen = set()
        for r in range(len(s)):
            while s[r] in CharSeen:
                CharSeen.remove(s[l])
                l+=1
            CharSeen.add(s[r])
            res = max(res,r-l+1)
        return res
        