class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_speed = 1
        max_speed = max(piles)

        res = 0
        while min_speed <= max_speed:
            mid = (max_speed + min_speed) // 2

            hours = 0
            for pile in piles:
                hours += math.ceil(pile / mid)
            if hours <= h:
                res = mid
                max_speed = mid - 1
            elif hours > h:
                min_speed = mid + 1
        return res

