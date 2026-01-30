class Solution: #TC: O(n) SP: O(n)
    def longestWPI(self, hours: List[int]) -> int:
        # Prefix + HashMap
        first_index = {}
        score = 0
        max_len = 0
        for i in range(len(hours)):
            if hours[i]>8:
                score += 1
            else:
                score -=1

            if score>0:
                max_len = i+1
            else:
                if (score-1) in first_index:
                    max_len = max(max_len,i-first_index[score-1])
            if score not in first_index:
                first_index[score]=i

        return max_len