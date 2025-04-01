class Solution:
    def maxSubArray(self, nums: List[int]) -> int:       
        summ = 0
        maxS = float('-inf')
        for n in nums:
            summ +=n #adding each element
            if summ > maxS: #updating for highest sum
                maxS = summ    
            if summ<0:  # Sum reset to get higher values
                summ = 0
            
        return maxS