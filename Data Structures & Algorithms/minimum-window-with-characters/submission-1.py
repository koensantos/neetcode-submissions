from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT, window = {}, {}

        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)
        res, resLen = [-1,-1], float("infinity")

        left = 0

        for right in range(0, len(s)):
            c = s[right]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                window[s[left]] -= 1
                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    have -= 1
                if ((right - left + 1)) < resLen:
                    resLen = (right - left + 1)
                    res = [left, right]
                left += 1
        l, r = res
        return s[l:r+1] if resLen < float("infinity") else ""