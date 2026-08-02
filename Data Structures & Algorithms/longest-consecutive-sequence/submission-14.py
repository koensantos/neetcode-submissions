class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest_sequence = 0
        #for num in nums:
            #check if left neighbor of current number is in the set
            #if yes:
                #sequence goes up
            #if no:
                #continue
        for num in nums_set:
            if (num - 1) not in nums_set:
                sequence = 0
                while sequence + num in nums_set:
                    sequence += 1
                longest_sequence = max(sequence, longest_sequence)

        return longest_sequence


        


        

        