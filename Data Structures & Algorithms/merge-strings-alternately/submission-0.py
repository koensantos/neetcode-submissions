class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        pointer1 = 0
        pointer2 = 0

        output = ""
        while pointer1 < len(word1) or pointer2 < len(word2):
            if pointer1 == len(word1):
                output += word2[pointer2]
                pointer2 += 1
            elif pointer2 == len(word2):
                output += word1[pointer1]
                pointer1 += 1
            else:
                output += word1[pointer1]
                output += word2[pointer2]
                pointer1 += 1
                pointer2 += 1
        return output
