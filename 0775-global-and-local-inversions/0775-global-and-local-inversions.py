class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        # For permutations of 0..n-1, all global inversions are local
        # iff every element is at most 1 position away from original index.
        return all(abs(nums[i] - i) <= 1 for i in range(len(nums)))