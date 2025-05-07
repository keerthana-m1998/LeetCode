class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # convert numbers to strings
        str_nums = list(map(str,nums))
        
        # Custome compare operator
        def compare(n1,n2):
            if n1 + n2 > n2 + n1: 
                return -1 # n1 should come first
            else:
                return 1 # n2 should come first
        # Sort using the comparator
        str_nums.sort(key=cmp_to_key(compare))

        # Join and handle leading zeros
        result = "".join(str_nums)
        return result if result[0]!='0' else '0' # return '0' if result = "0000"
        