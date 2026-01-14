class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # if c==1:
        #     return True
        # if c==2:
        #     return True
        left,right=0,int(math.sqrt(c))
        while left<=right:
            square_sum = left*left + right*right
            if square_sum == c:
                return True
            elif square_sum<c:
                left+=1
            else:
                right-=1
        return False