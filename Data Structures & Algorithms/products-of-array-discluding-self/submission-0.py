class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref = [0] * n
        suf = [0] * n
        pref[0] = suf[n-1] = 1

        for i in range(1, len(nums)):
            pref[i] = pref[i-1] * nums[i-1]
        
        for i in range(len(nums)-2, -1, -1):
            suf[i] = suf[i+1] * nums[i+1]
        
        res = [0]*n

        for i in range(len(pref)):
            res[i] = pref[i]*suf[i]

        return res