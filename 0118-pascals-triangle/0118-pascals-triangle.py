class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        def generatoR(row:int) -> List[int]:
            ans = 1
            ansRow = [1]
            for col in range(1,row):
                ans = ans*(row-col)
                ans = ans//col
                ansRow.append(ans)
            return ansRow
        ans = []
        for row in range(1,numRows+1):
            ans.append(generatoR(row))
        return ans