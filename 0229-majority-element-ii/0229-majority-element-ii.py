class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # n = len(nums)
        # # # Using HashMAP
        # # res = []
        # # counter = Counter(nums) #HashMap to count occurences
        # # for num,count in counter.items():
        # #     if count>(n/3):
        # #         res.append(num)
        # # return res

        if not nums:
            return []

        # 1st pass: find up to two candidates
        candidate1 = candidate2 = None
        count1 = count2 = 0

        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1 = num
                count1 = 1
            elif count2 == 0:
                candidate2 = num
                count2 = 1
            else:
                # current num is different from both candidates
                # and both counts are non-zero → cancel out
                count1 -= 1
                count2 -= 1

        # 2nd pass: verify the candidates
        result = []
        n = len(nums)
        c1 = nums.count(candidate1) if candidate1 is not None else 0
        c2 = nums.count(candidate2) if candidate2 is not None else 0

        if c1 > n // 3:
            result.append(candidate1)
        # need candidate2 != candidate1 to avoid duplicates
        if candidate2 is not None and candidate2 != candidate1 and c2 > n // 3:
            result.append(candidate2)

        return result