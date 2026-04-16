from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # let's follow sliding window approach
        # initial idea is to have a window and count\
        n, l = len(s), 0
        mpp = {}
        maxf = 0
        longest = 0
        for r in range(n):
            mpp[s[r]] = mpp.get(s[r], 0) + 1
            maxf = max(mpp[s[r]], maxf)
            while (r-l+1) - maxf > k:
                mpp[s[l]]-=1
                l+=1
            longest = max(longest, r-l+1)
        return longest
