class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        num_list = []
        num_list = list(num) # Convert num to list of str
        mutated = False # track to check if further mutation is needed or break
        for i in range(len(num)):
            d = int(num_list[i]) 
            if change[d]>d: # Compare
                num_list[i] = str(change[d]) # Change
                mutated = True
            elif change[d]<d:
                if mutated: # break, no pint in mutating further
                    break #  as it will only reduce the number
        return ''.join(num_list)