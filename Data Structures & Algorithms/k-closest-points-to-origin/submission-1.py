class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        min_dist = 999
        for x , y in points:
            dist = x*x + y*y
            heapq.heappush(heap,[-dist,x,y])
            while(len(heap)>k):
                heapq.heappop(heap)
        return [[x,y] for _, x, y in heap]