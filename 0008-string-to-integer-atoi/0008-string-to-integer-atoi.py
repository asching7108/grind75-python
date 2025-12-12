class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0

        n = len(s)
        i = 0
        sign = 1
        res = 0

        INT_MAX = pow(2, 31) - 1
        INT_MIN = -pow(2, 31)

        # Remove leading whitespace
        while i < n and s[i] == ' ':
            i += 1

        # Determine signedness
        if i < n and s[i] == '-':
            sign = -1
            i += 1
        elif i < n and s[i] == '+':
            i += 1

        # Remove leading 0s
        # while i < len(s) and s[i] == '0':
        #     i += 1

        # Read digits
        while i < len(s) and s[i].isdigit():
            digit = int(s[i])

            # Check overflow and underflow conditions
            if (res > INT_MAX // 10) or (
                res == INT_MAX // 10 and digit > INT_MAX % 10
            ):
                return INT_MAX if sign == 1 else INT_MIN

            # Append current digit
            res = res * 10 + digit
            i += 1

        return res * sign

# Time complexity: O(n)
# Space complexity: O(1)