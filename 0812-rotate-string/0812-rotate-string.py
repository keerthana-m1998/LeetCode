class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # shortcut Soln: if lengths are not equal, return False
        # concatinate s --> abcdeabcde , check if goal is present
        # a'bcdea'bcde  --> "bcdea" ==> returns True
        return len(s)==len(goal) and goal in (s+s) 
        # TC : O(N), SC : O(s+s)

        # SImulate Rotation Soln:
        
        for _ in s:
            if s==goal:
                return True
            s = s[1:]+s[0]
        return False

        