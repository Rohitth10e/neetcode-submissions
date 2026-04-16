class Solution:
    def lcs(self, nums, sorted_num, n, m, memo):
        if n < 0 or m < 0:
            return 0

        if memo[n][m]:
            return memo[n][m]
        
        if nums[n] == sorted_num[m]:
            memo[n][m] = 1 + self.lcs(nums, sorted_num, n-1, m-1, memo)
        else:
            memo[n][m] = max(self.lcs(nums, sorted_num, n-1, m, memo), self.lcs(nums, sorted_num, n, m-1, memo))
        return memo[n][m]

    def lengthOfLIS(self, nums: List[int]) -> int:

        sorted_num = sorted(set(nums))
        n = len(nums) - 1
        m = len(sorted_num) - 1
        memo = [[0]*(m+1) for _ in range(n+1)]

        self.lcs(nums, sorted_num, n, m, memo)
        return memo[n][m]