class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        num_unique = len(set(nums))
        nums[:num_unique] = sorted(set(nums))
        return num_unique
