import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        hashmap = Counter(nums)

        for key, val in hashmap.items():
            if len(heap) == k:
                heapq.heappushpop(heap, (val, key))
            else:
                heapq.heappush(heap, (val, key))
        return [i[1] for i in heap]