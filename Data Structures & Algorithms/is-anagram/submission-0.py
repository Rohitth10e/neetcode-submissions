class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_s = sorted(s)
        sorted_t = sorted(t)

        if len(s) != len(t):
            return False

        return "".join(sorted_s) == "".join(sorted_t)