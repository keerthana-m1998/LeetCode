class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        row = 0
        col = m-1
        while row<n and col>=0:
            if matrix[row][col]==target:
                return True
            elif matrix[row][col]>target:
                col-=1
            else:
                row+=1
        return False