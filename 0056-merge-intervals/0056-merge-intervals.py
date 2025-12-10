class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Step 1: Sort by starting time
        intervals.sort(key=lambda x: x[0])
        
        merged = []

        for interval in intervals:
            # If merged list is empty OR no overlap → add interval
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # Overlap → merge by extending the end
                merged[-1][1] = max(merged[-1][1], interval[1])
        
        return merged
        