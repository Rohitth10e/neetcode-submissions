class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mpp = {}

        for idx, num in enumerate(nums):
            diff = target - num
            if diff in mpp:
                return [mpp[diff], idx]
            mpp[num] = idx
        # return []