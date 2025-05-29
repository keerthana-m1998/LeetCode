class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(n):
            while (
                1 <= nums[i] <= n
                and nums[nums[i] - 1] != nums[i]
            ):
                # Swap nums[i] to its correct position
                correct_idx = nums[i] - 1
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]

        # After rearrangement, first index i where nums[i] != i + 1 is the answer
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1
            