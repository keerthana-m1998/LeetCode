class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        height_name = {}
        res = []
        for h,n in zip(heights,names):
            height_name[h] = n
            
        for i in reversed(sorted(heights)):
            res.append(height_name[i])
        return res