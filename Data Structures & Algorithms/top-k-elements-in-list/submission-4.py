import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)

        # heap = []
        # for key, val in freq.items():
        #     heapq.heappush(heap , [val, key])
        #     if len(heap) > k:
        #         heapq.heappop(heap)

        bucket = [[] for i in range(len(nums)+1)]
        for num, f in freq.items():
            bucket[f].append(num)

        
        res = []
        for i in range(len(bucket)-1 , 0 ,-1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res
