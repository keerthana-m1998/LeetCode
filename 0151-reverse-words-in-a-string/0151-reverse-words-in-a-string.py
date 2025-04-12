class Solution:
    def reverseWords(self, s: str) -> str:
        # # SHortcut using SPLIT Function
        # return ' '.join(reversed(s.split()))
        # Manual processing
        words = []
        current_word = []
        for c in s:
            if c!=' ':
                current_word.append(c)
            elif current_word:
                words.append(''.join(current_word))
                current_word = []
        if current_word:
            words.append(''.join(current_word))

        return " ".join(reversed(words))
        