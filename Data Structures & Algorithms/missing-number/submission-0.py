class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor = len(nums)
        for idx , num in enumerate(nums):
            xor^= idx ^ num
        return xor