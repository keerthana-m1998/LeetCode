class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # HAshmap uses extra memory O(n), O(n)
        # hashmap = {}
        # counter,res = 0,0
        # for n in nums:
        #     hashmap[n] = 1+hashmap.get(n,0)
        #     res = n if hashmap[n]>counter else res
        #     counter = max(hashmap[n],counter) 
        # return res

        #(Boyer-Moore Voting)
        counter = 0
        candidate = None
        for n in nums:
            if counter == 0:
                candidate = n
            counter += (1 if candidate == n else -1)
        return candidate
        