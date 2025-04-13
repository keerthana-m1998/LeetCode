class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # 2 strings are ISOMORPHIC if you can replace every CHAR from one string with a unique character in another string, while preserving order


        # Shorcut, record the first index of each character where it appears
        # ex: paper , title
        # s = [0,1,0,3,4], [0,1,0,3,4]

        # return [s.index(c) for c in s] == [t.index(c) for c in t] 

        #1 
        if len(s)!=len(t):
            return False
        #2 Character mapping: use 2 dictionaries to keep track of char mapping
        # s->t , t->s

        s_to_t = {}
        t_to_s = {}
        
        for s_char,t_char in zip(s,t):
            # Check for s->t mapping
            if s_char in s_to_t:
                if s_to_t[s_char] != t_char:
                    return False
            else:
                s_to_t[s_char]=t_char

            # Check for t->s mapping
            if t_char in t_to_s:
                if t_to_s[t_char]!=s_char:
                    return False
            else:
                t_to_s[t_char]=s_char
        return True

            
        