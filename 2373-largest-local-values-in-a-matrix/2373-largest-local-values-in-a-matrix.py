class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        # Build a n-2*n-2 matrix scanning 3*3 grid tracking max value
        n = len(grid) # length of matrix
        res = [[0]*(n-2) for _ in range(n-2)] # built 0 matrix of (n-2)*(n-2)

        for i in range(n-2): # row for top-left of 3x3
            for j in range(n-2):  # col for top-left of 3x3

                max_val = 0     # Reset max_val for each 3*3 grid

                # scan 3*3 grid for each i,j
                for r in range(i,i+3):
                    for c in range(j,j+3):
                        max_val = max(max_val, grid[r][c])
                res[i][j] = max_val # update max_val in (n-2)*(n-2) result matrix
        return res

        