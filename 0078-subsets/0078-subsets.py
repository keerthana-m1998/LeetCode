class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []

        def backtrack(index):
            # Base case: we have considered all elements
            if index == len(nums):
                # Add a copy of current subset
                result.append(path[:])
                return

            # Choice 1: do NOT include nums[index]
            backtrack(index+1)

            # Choice 2: include nums[index]
            path.append(nums[index])
            backtrack(index+1)
            path.pop()  # backtrack

        backtrack(0)
        return result


        """Core idea (say this clearly)
            At each index:
            Either include the element
            Or exclude it
            We explore both paths."""


# Time: O(2^n)
# Space: O(n) recursion depth
# (output space not counted)

        