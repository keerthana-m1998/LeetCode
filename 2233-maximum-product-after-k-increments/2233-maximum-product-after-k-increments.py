class Solution:
    """
    🔑 Intuition (say this clearly)
    To maximize the product:
    We should increase the smallest number first
    Increasing a small number gives more multiplicative gain than increasing a large
    one
    
    📌 This is a classic greedy equalization problem.

    Time: O(k log n)
    Space: O(n)
    
    """
    def maximumProduct(self, nums: List[int], k: int) -> int:
        product = 1
        MOD = 10**9+7

        # Convert list into a min-heap
        heapq.heapify(nums)

        # Perform k increments
        for _ in range(k):
            smallest = heapq.heappop(nums)
            smallest +=1
            heapq.heappush(nums,smallest)

        # Compute product modulo MOD
        for num in nums:
            product = (product*num)%MOD

        return product

        # “At each step, incrementing the smallest value increases the total product more than incrementing any larger value. A min-heap allows us to always apply this greedy choice efficiently.”

        

        # “I used a greedy strategy with a min-heap, always incrementing the smallest element to maximize the final product. This runs in O(k log n) time and O(n) space.”