class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        mat = [[0]*n for _ in range(n)]
        left,right = 0,n-1
        top,bottom = 0,n-1
        val = 1
        while left<=right:
        # add on top part--> left to right
            for c in range(left,right+1):
                mat[top][c]=val
                val+=1
            top+=1
        # add on right side-->top to bottom
            for r in range(top,bottom+1):
                mat[r][right] = val
                val+=1
            right-=1

        # add in bottom, right to left ( reverse)
            for c in range(right,left-1,-1):
                mat[bottom][c] = val
                val+=1
            bottom-=1

        # add in left, bottom to top ( reverse)
            for r in range(bottom,top-1,-1):
                mat[r][left]=val
                val+=1
            left+=1
        return mat        