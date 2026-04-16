class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        h={}
        l, maxlen = 0,0

        for r in range(len(s)):
            if s[r] in h:
                if h[s[r]] >= l:
                    l = h[s[r]] + 1
            h[s[r]] = r
            maxlen = max(maxlen, r-l+1)
        return maxlen