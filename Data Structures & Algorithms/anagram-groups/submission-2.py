class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mpp = defaultdict(list)
        for s in strs:
            sorted_s = "".join(sorted(s))
            if sorted_s in mpp:
                mpp[sorted_s].append(s)
            else:
                mpp[sorted_s] = [s]
        
        return list(mpp.values())