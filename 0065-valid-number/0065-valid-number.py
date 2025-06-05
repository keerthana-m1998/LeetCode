class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        num, dot, exp = False, False, False

        for i, char in enumerate(s):
            if char.isdigit():
                num = True
            elif char in ['+', '-']:
                if i > 0 and s[i - 1] not in ['e', 'E']:
                    return False
            elif char == '.':
                if dot or exp:
                    return False
                dot = True
            elif char in ['e', 'E']:
                if exp or not num:
                    return False
                exp = True
                num = False  # reset for the exponent part
            else:
                return False

        return num