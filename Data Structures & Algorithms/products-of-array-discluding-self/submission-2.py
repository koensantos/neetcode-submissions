class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        output = [1] * len(nums)

        for i in range(0,len(nums)):
            output[i] = prefix
            prefix *= nums[i]
        
        postfix = 1

        j = len(nums) - 1

        while j >= 0:
            output[j] *= postfix
            postfix *= nums[j]
            j -= 1
        return output