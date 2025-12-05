class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        max_row = 0
        max_ones = 0
        for row, ones in enumerate(mat):
            ones_count = sum(ones)
            if ones_count>max_ones:
                max_ones = ones_count
                max_row = row
        return [max_row,max_ones]

