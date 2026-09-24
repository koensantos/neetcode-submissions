class Solution:
    from heapq import heapify, heappush, heappop
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #Get list of distances to k per point.
        #Sort and get k closest

        distances = []

        for point in points:
            distance = point[0] ** 2 + point[1] ** 2
            distances.append([distance, point[0], point[1]])

        heapq.heapify(distances)

        res = []

        while k > 0:
            distance, x, y = heapq.heappop(distances)
            res.append([x,y])
            k -= 1
        return res
            

        