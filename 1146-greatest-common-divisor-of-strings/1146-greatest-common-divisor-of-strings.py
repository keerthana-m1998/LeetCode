class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # str1 = "ABCABCD", str2 = "ABC"
        # ABCABCD ABC != ABC ABCABCD
        if str1 + str2 != str2 + str1:
            return ""
        # if equal implies GCD of str1 and str2 will be the biggest string i.e GCD of str1 and str2
        size = math.gcd(len(str1),len(str2))
        return str1[:size]
        