class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # combinatorics
        ansRow = [1]
        ans = 1
        row = rowIndex+1
        for col in range(1,row):
            ans = ans*(row-col)
            ans = ans//col 
            ansRow.append(ans)
        return ansRow

