class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        m = {}
        l = 0
        longest, freq = 0, 0
        for r in range(len(s)):
            m[s[r]] = m.get(s[r], 0) + 1
            freq = max(m[s[r]], freq)
            while (r-l+1) - freq > k:
                m[s[l]] -=1
                l+=1
            longest = max(r-l+1, longest)
        return longest
