class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mpp=defaultdict(list)

        for s in strs:
            sorted_str = "".join(sorted(s))
            if sorted_str not in mpp:
                mpp[sorted_str] = [s]
            else:
                mpp[sorted_str].append(s)
        
        return list(mpp.values())