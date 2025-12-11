class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        MOD = 10**9 + 7
        
        # 1) compute all subarray sums (O(n^2))
        subs = []
        for i in range(n):
            s = 0
            for j in range(i, n):
                s += nums[j]
                subs.append(s)
        
        # 2) sort them (O(m log m), m = n*(n+1)//2)
        subs.sort()
        
        # 3) prefix sums of sorted list to answer range sum quickly
        # prefix[k] = sum of subs[0..k-1], prefix[0] = 0
        m = len(subs)
        prefix = [0] * (m + 1)
        for i in range(1, m + 1):
            prefix[i] = (prefix[i-1] + subs[i-1]) % MOD
        
        # left and right are 1-indexed in problem statement
        ans = (prefix[right] - prefix[left - 1]) % MOD
        return ans