class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = []
        counter = 0
        #Track balance of paranthesis +1 or -1
        # Identify primitives: whenbalance returns to zero, it's primitive
        for c in s:
            if c == '(':
                if counter>0: #check to skip outermost paranthesis
                    res.append(c) # Append only the inner paranthesis
                counter+=1 # count all paranthesis
            else:
                counter-=1  # decrement for '('
                if counter>0:
                    res.append(c) # Append only the inner paranthesis
        return ''.join(res) # join to return in string 
        