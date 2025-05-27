class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # res = []
        # def dfs(i,cur,total):
        #     if total == target:
        #         res.append(cur.copy()) # append a copy to avoid changing cur
        #     if i>=len(candidates) or total > target:
        #         return 
        #     cur.append(candidates[i])
        #     dfs(i,cur,total+candidates[i])
        #     cur.pop()
        #     dfs(i+1,cur,total)

        # dfs(0,[],0)
        # return res

        def backtrack(start,path,remaining):
            if remaining == 0:
                res.append(path.copy())
                return 
            for i in range(start,len(candidates)):
                if candidates[i]>remaining:
                    continue
                path.append(candidates[i])
                backtrack(i,path,remaining-candidates[i])
                path.pop()
        res = []
        candidates.sort()
        backtrack(0,[],target)
        return res