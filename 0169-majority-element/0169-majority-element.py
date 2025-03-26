class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}
        counter,res = 0,0
        for n in nums:
            hashmap[n] = 1+hashmap.get(n,0)
            res = n if hashmap[n]>counter else res
            counter = max(hashmap[n],counter)
        return res
        