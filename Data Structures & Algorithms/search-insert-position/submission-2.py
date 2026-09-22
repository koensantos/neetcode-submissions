class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        output = len(nums)
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2
            if target == nums[mid]:
                return mid
            if nums[mid] < target:
                l = mid + 1
            else:
                output = mid
                r = mid - 1
        return output