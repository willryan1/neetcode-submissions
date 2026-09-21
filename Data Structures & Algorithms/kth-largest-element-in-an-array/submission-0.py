class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap_max = [-x for x in nums]
        heapq.heapify(heap_max)
        for i in range(k-1):
            heapq.heappop(heap_max)
        return -heapq.heappop(heap_max)