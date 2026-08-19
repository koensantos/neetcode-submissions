class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        min_length = float("infinity")
        l = 0
        total = 0

        for r in range(0,len(nums)):
            total += nums[r]
            while total >= target:
                min_length = min(r - l + 1, min_length)
                total -= nums[l]
                l+= 1

        if min_length == float("infinity"):
            return 0
        else:
            return min_length    
