class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7  # constraint given
        heapq.heapify(nums) # Heapify nums into Min_heap

        for _ in range (k):
            smallest = heapq.heappop(nums) # pop smallest
            heapq.heappush(nums,smallest+1) #increment n push smallest

        product = 1
        for num in nums:
            product = (product*num)%MOD  # Modulo @ each step to prevent overflow

        return product
        