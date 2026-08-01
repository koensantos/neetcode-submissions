class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest_sequence = 0
        #for num in nums:
            #check if left neighbor of current number is in the set
            #if yes:
                #sequence goes up
            #if no:
                #continue
        for num in nums:
            if (num - 1) not in nums:
                sequence = 0
                while(num + sequence) in nums:
                    sequence += 1
                longest_sequence = max(longest_sequence, sequence)
        return longest_sequence



        


        

        