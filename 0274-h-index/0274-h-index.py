class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # # Sort citations in descending order
        # citations.sort(reverse=True)
        # h = 0
        # # i is 0-based, so h = i+1
        # for i,c in enumerate(citations):
        #     if c>=i+1:
        #         h = i+1
        #     else:
        #         break
        # return h

        n = len(citations)
        # count[i] = how many papers have exactly i citations (for i in [0, n])
        # citations > n are bucketed into count[n]
        count = [0] * (n + 1)
        
        for c in citations:
            if c >= n:
                count[n] += 1
            else:
                count[c] += 1
        
        papers_with_at_least_h = 0
        # Go from h = n down to 0
        for h in range(n, -1, -1):
            papers_with_at_least_h += count[h]
            if papers_with_at_least_h >= h:
                return h
        
        return 0