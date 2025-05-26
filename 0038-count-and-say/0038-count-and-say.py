class Solution:
    def countAndSay(self, n: int) -> str:
        # IBH Method
        if n==1: # Base condition   
            return "1"
        prev = self.countAndSay(n-1) # Hypothesis
        res = []
        i = 0

        # Induction
        while i < len(prev):
            count = 1
            while i+1<len(prev) and prev[i]==prev[i+1]:
                count +=1
                i+=1
            res.append(f"{count}{prev[i]}")
            i+=1
        return "".join(res)