class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)

        low, high = 1, max(piles)

        while low <= high:
            mid = low + (high - low) // 2

            currTotal = 0
            for i in range(n):
                currTotal += math.ceil(piles[i] / mid)
            
            if currTotal <= h:
                high = mid - 1
            else:
                low = mid + 1
        return low