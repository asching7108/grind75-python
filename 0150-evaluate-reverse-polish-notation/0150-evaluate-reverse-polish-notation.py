class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b)
        }

        stack = []

        for curr in tokens:
            if curr not in operations:
                stack.append(int(curr))
            else:
                val2 = stack.pop()
                val1 = stack.pop()
                stack.append(operations[curr](val1, val2))

        return stack.pop()

# Time complexity: O(n)
# Space complexity: O(n)