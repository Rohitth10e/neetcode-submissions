class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []

        for num in stones:
            heapq.heappush(heap, -num)
        while len(heap) > 1:
            num1 = heapq.heappop(heap)
            num2 = heapq.heappop(heap)
            if num1 < num2:
                heapq.heappush(heap, num1-num2)
        heapq.heappush(heap,0)
        return abs(heap[0])