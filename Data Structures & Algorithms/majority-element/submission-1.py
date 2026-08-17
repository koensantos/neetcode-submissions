class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #[1,1,1,5,5,5,5]
        hashmap = Counter(nums)
        print(hashmap)

        output = 0
        freq = 0
        for k, v in hashmap.items():
            if v > freq:
                freq = v
                output = k
        return output
         