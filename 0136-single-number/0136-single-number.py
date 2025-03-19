class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # xor=0
        # for i in nums:  # 0^0 = 0
        #     xor ^= i    # 0^1 = 1
        # return xor      # 1^0 = 1
        #                 # 1^1=0
        
        #RPGM 19-03-2025
        xor = 0
        for i in nums:
            xor ^=i
        return xor