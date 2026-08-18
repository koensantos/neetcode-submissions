class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = 0
        window = {}

        for r in range(0,len(nums)):
            if abs(l - r) > k:
                window[nums[l]] -= 1
                l += 1
            if nums[r] in window and window[nums[r]] > 0:
                return True
            else:
                window[nums[r]] = 1 + window.get(nums[r], 0)
                
        return False
