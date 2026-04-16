class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        h = {}
        l = 0
        n = len(s)
        max_len = 0
        for r in range(n):
            if s[r] in h:
                if h[s[r]] >= l:
                    l = h[s[r]] + 1
            max_len = max(max_len, r-l+1)
            h[s[r]] = r
        return max_len