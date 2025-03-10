class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i :i[0]) #Sort based on first element
        output = [intervals[0]] # initialize output with first list
        for start,end in intervals[1:]: # start from 2nd element
            lastEnd = output[-1][1] # assign last range end to VAR "lastEnd"
            if start <= lastEnd: # compare if intervals merge
                output[-1][1]=max(end,lastEnd) # update the range of intervals
            else:
                output.append([start,end]) # for disconnected intervals, append to output 
        return output  