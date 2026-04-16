class Solution:
    def lcs(self, nums, sorted_num, n, m):
        if n < 0 or m < 0:
            return 0
        
        if nums[n] == sorted_num[m]:
            return 1 + self.lcs(nums, sorted_num, n-1, m-1)
        else:
            return max(self.lcs(nums, sorted_num, n-1, m), self.lcs(nums, sorted_num, n, m-1))

    def lengthOfLIS(self, nums: List[int]) -> int:

        sorted_num = sorted(set(nums))
        n = len(nums) - 1
        m = len(sorted_num) - 1

        return self.lcs(nums, sorted_num, n, m)