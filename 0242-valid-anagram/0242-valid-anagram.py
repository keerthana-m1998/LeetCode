from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # ANAGRAM 1--> exactly the same letters
        # 2--> Same frequency (count) of each letter
        # Method 1:
        # return Counter(s)==Counter(t) # Built_in SHortcut

        # Method 2:
        # s_count = Counter(s)
        # for char in t:
        #     if char not in s_count:
        #         return False
        #     s_count[char] -=1
        #     if s_count[char]==0:
        #         del s_count[char]
        # return len(s_count)==0

        # Method 3:
        s_Table = {}
        t_Table = {}

        for c in s:
            s_Table[c] = s_Table.get(c,0)+1
        for c in t:
            t_Table[c] = t_Table.get(c,0)+1

        return s_Table == t_Table
        