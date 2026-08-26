class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        nums_list = sorted(list(set(nums)))

        l = 0
        r = len(nums_list) - 1

        while l < r:
            m = l + (r - l) // 2
            if nums_list[m] > nums_list[r]:
                l = m + 1
            else:
                r = m
        pivot = l

        def binary(l: int, r: int) -> bool:
            while l <= r:
                m = l + (r - l) // 2
                if nums_list[m] == target:
                    return True
                elif nums_list[m] > target:
                    r = m - 1
                else:
                    l = m + 1
            return False
        
        if binary(0, pivot - 1) == True:
            return True
        else:
            return binary(pivot, len(nums_list) - 1)
