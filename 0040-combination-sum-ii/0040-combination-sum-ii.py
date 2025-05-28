class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(start,path,remaining):
            if remaining == 0:
                res.append(path.copy())
                return 
            for i in range(start,len(candidates)):
                if candidates[i]>remaining:
                    break
                if candidates[i]==candidates[i-1] and i>start:
                    continue
                path.append(candidates[i])
                backtrack(i+1,path,remaining-candidates[i])
                
                path.pop()
                
        candidates.sort()
        backtrack(0,[],target)
        return res