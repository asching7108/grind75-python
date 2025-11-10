class Solution:
    # Recursion with Memoization
    # def climbStairs(self, n: int) -> int:
    #     memo = [0] * (n + 1)
    #     return self.climbStairsHelper(0, n, memo)

    # def climbStairsHelper(self, i: int, n: int, memo: List[int]) -> int:
    #     if i > n:
    #         return 0
    #     if i == n:
    #         return 1
    #     if memo[i] == 0:
    #         memo[i] = (
    #             self.climbStairsHelper(i + 1, n, memo) +
    #             self.climbStairsHelper(i + 2, n, memo)
    #         )
    #     return memo[i]
    
    # Time complexity: O(n)
    # Space complexity: O(n)

    # Dynamic Programming
    # def climbStairs(self, n: int) -> int:
    #     if n == 1:
    #         return 1
    #     dp = [0 for _ in range(n + 1)]
    #     dp[1] = 1
    #     dp[2] = 2
    #     for i in range(3, n + 1):
    #         dp[i] = dp[i - 1] + dp[i - 2]
    #     return dp[n]
    
    # Time complexity: O(n)
    # Space complexity: O(n)

    # Fibonacci Number
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        first = 1
        second = 2
        for i in range(3, n + 1):
            third = first + second
            first = second
            second = third
        return second
    
    # Time complexity: O(n)
    # Space complexity: O(1)
        
# f(n)=f(n−1)+f(n−2),f(1)=1,f(2)=2
# i.e. f(n)=Fib(n+1)