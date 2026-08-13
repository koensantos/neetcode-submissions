class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        length = 0
        left = 0
        for right in range(0, len(s)):
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1
            charSet.add(s[right])
            length = max(length, right - left + 1)
        return length


        
                