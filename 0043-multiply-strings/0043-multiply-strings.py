class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        m, n = len(num1), len(num2)
        result = [0] * (m + n)

        # Reverse for easier indexing (units at end)
        num1 = num1[::-1]
        num2 = num2[::-1]

        for i in range(m):
            for j in range(n):
                digit1 = int(num1[i])
                digit2 = int(num2[j])
                product = digit1 * digit2
                result[i + j] += product

                # Handle carry
                result[i + j + 1] += result[i + j] // 10
                result[i + j] %= 10

        # Remove leading zeros
        while len(result) > 1 and result[-1] == 0:
            result.pop()

        # Convert back to string
        return ''.join(map(str, result[::-1]))       