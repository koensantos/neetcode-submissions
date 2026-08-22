class Solution:
    def mySqrt(self, x: int) -> int:

        if x == 0:
            return 0
        
        low = 0
        high = x
        res = 0

        while low <= high:
            mid = low + (high - low) // 2
            if mid * mid == x:
                return mid
            if mid * mid > x:
                high = mid - 1
            else:
                res = mid
                low = mid + 1
        return res