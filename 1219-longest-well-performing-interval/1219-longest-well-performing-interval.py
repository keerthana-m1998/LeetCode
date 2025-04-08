class Solution: #TC: O(n) SP: O(n)
    def longestWPI(self, hours: List[int]) -> int:
        # Prefix + HashMap
        res = score = 0
        seen = {} # HashMap {score: first_occurence_indx}
        for i , h in enumerate(hours):
            score += h>8 # score +=1 if hours[i]> 8 
            score -= h<9 # score -=1 if hours[i]< 8 [1,1,-1,-1,-1,-1,9]
            if score >0: # SubArray 
                res = i+1 # Valid subarray from i, continous length will be updated in res  ## Greedy track to get max subarray
            seen.setdefault(score,i) # if score not in seen (Record first occurence)
            if score -1 in seen:
                res = max(res,i-seen[score-1])
        return res
        