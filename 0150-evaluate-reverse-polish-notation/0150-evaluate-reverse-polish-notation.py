class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def compute(val1: int, val2: int, operation: str) -> int:
            match operation:
                case "+":
                    return val1 + val2
                case "-":
                    return val1 - val2
                case "*":
                    return val1 * val2
                case "/":
                    return trunc(val1 / val2)
 
        operations = set(["+", "-", "*", "/"])
        stack = []

        for curr in tokens:
            if curr not in operations:
                stack.append(int(curr))
            else:
                right = stack.pop()
                left = stack.pop()
                stack.append(compute(left, right, curr))

        return stack[0]

# Time complexity: O(n)
# Space complexity: O(n)