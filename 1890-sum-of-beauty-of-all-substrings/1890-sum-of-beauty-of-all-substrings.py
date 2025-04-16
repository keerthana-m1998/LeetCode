class Solution:
    def beautySum(self, s: str) -> int:
        # Brute force works
        # For each possible substring, track freq
        # calculate beauty as max_freq-min_freq
        # add it to beauty_sum
        beauty_sum = 0
        for i in range(len(s)):
            freq = {} # Array can be used too
            #reset freq for new substrings starting at i
            for j in range(i,len(s)):
            #update freq s[j]
                freq[s[j]] = freq.get(s[j],0)+1
                if len(freq)>=2:
                    min_freq = min(freq.values())
                    max_freq = max(freq.values())
                    beauty_sum += (max_freq-min_freq)
        return beauty_sum  
         # O(N*N), O(1) for fixed freq dictionary ( 26 letter)      