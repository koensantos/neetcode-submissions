class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        for i in range(0, len(s2) - len(s1) + 1):
            substring = s2[i:len(s1) + i]
            hash1 = Counter(substring)
            hash2 = Counter(s1)
            if hash1 == hash2:
                return True
        return False