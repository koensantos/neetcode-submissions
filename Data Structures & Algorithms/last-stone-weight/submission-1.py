class Solution:
    from heapq import heapify, heappop, heappush
    def lastStoneWeight(self, stones: List[int]) -> int:
        #For every iteration until len of stones <= 1
            #Sort stones
            #take last 2 stones
            #if 1 stone is greater than the other:
                #Take difference and append back to stones
        #if len == 1:
            #return the stone
        #if len < 1:
            #return 0

        while len(stones) > 1:
            stones = sorted(stones)
            stone1 = stones.pop()
            stone2 = stones.pop()
            if abs(stone1 - stone2) != 0:
                stones.append(abs(stone1 - stone2))
        if len(stones) == 1:
            return stones[0]
        else:
            return 0

        