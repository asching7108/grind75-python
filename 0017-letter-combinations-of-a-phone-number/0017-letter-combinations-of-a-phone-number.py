class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Map all the digits to corresponding letters
        letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        results = []

        def backtrack(index, path):
            if len(path) == len(digits):
                results.append(''.join(path))
                return

            for letter in letters[digits[index]]:
                path.append(letter)
                backtrack(index + 1, path)
                path.pop()

        backtrack(0, [])
        return results

# Time complexity: O(4^n * n), O(4^n) for backtrack and O(n) for building the combination
# Space complexity: O(n) for the recursion stack