class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left,right = 0,len(numbers)-1
        ans = []
        while left<=right:
            summ = numbers[left]+numbers[right]
            if summ == target:
                ans.append(left+1)
                ans.append(right+1)
                return ans
            elif summ<target:
                left+=1
            else:
                right -=1
        return ans
        
        