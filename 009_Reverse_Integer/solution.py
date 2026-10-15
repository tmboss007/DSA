class Solution:
    def reverse(self, x: int) -> int:

        INT_MIN = -2147483648
        INT_MAX = 2147483647

        sign = -1 if x < 0 else 1
        x = abs(x)

        result = 0
        limit = INT_MAX if sign == 1 else 2147483648

        while x > 0:
            digit = x % 10
            x //= 10

            if result > limit // 10 or (
                result == limit // 10 and digit > limit % 10
            ):
                return 0

            result = result * 10 + digit

        return result * sign