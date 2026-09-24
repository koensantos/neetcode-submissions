class Solution:
    from heapq import heapify, heappop, heappush
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []
        #We want the larger nums in num
        #Use max heap
        #For each num in nums:
            #if not heap:
                #append to heap
            #if num < max(heap):
                #dont append
            #else

        heapq.heapify(minHeap)
        for num in nums:
            heapq.heappush(minHeap, num)
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        return minHeap[0]