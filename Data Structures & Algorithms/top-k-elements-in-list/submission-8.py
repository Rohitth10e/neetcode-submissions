class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        mpp=  {}

        for num in nums:
            mpp[num] = mpp.get(num, 0) + 1


        for key in mpp.keys():
            heapq.heappush(heap,(mpp[key], key))
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res