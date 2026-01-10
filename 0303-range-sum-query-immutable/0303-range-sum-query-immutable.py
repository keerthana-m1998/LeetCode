class NumArray:

    def __init__(self, nums: List[int]):
        # Build prefix sum array       
        # prefix[i] = sum of nums[0] to nums[i-1]
        self.prefix = [0]
        for num in nums:
            self.prefix.append(self.prefix[-1] + num)

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right+1]-self.prefix[left]
        
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)


# Index:      0   1   2   3   4   5
# nums:     [-2,  0,  3, -5,  2, -1]

# prefix:  [0, -2, -2,  1, -4, -2, -3]
#           ↑   ↑   ↑   ↑   ↑   ↑   ↑
#           │   │   │   │   │   │   └─ sum of all 6 elements
#           │   │   │   │   │   └─ sum of first 5 elements
#           │   │   │   │   └─ sum of first 4 elements
#           └─ sum of 0 elements (empty)

# Query: sumRange(2, 5)
# prefix[6] - prefix[2] = (-3) - (-2) = -1 ✓
# O(N),O(N)