class Solution:
    def helper(self, n, dp):
        if n <= 2:
            return n
        if n in dp:
            return dp[n]
        dp[n] = self.helper(n-1,dp) + self.helper(n-2, dp)
        return dp[n]

    def climbStairs(self, n: int) -> int:
        dp = {}
        return self.helper(n, dp)