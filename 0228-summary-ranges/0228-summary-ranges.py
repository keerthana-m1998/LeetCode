class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        if not nums:
            return res
        start = nums[0] # start of current range
        
        for i in range(1,len(nums)):
            # If current is not consecutive to previous, we close the current range
            if nums[i] != nums[i-1]+1:
                if nums[i-1]==start:
                    # single element range
                    res.append(str(start))
                else:
                    res.append(f"{start}->{nums[i-1]}")
                # start a new range    
                start = nums[i]

        # Handle the last range after loop ends
        if nums[-1]==start:
            res.append(str(start))
        else:
            res.append(f"{start}->{nums[-1]}")
        return res
        