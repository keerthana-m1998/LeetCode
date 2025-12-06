class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        row = len(grid)
        col = len(grid[0])
        # RULE 1: Check all rows alternate (no two horizontal adjacent cells equal)
        for r in range(row):
            for c in range(1,col):
                if grid[r][c]==grid[r][c-1]:
                    return False    # violates alternating rule

        # RULE 2: Check column uniformity (all rows must match first row pattern)
        for c in range(col):
            for r in range(1,row):
                if grid[r][c] != grid[0][c]:
                    return False    # column pattern mismatch
        return True