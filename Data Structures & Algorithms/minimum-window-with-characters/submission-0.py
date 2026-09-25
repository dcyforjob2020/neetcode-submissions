class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""

        countT, window = {}, {}

        for c in t:
            countT[c] = countT.get(c, 0) + 1

        have, need = 0, len(countT)

        l = 0
 
        for r in range(len(s)):
            c = s[r]

            if c in countT:
                window[c] = window.get(c, 0) + 1

                if window[c] == countT[c]:
                    have += 1

                    while have == need:
                        if res == "":
                            res = s[l: r + 1]
                        elif len(res) > r - l + 1:
                            res = s[l: r + 1]

                        left_c = s[l]

                        if left_c in countT:
                            window[left_c] = window.get(left_c, 0) - 1
                            if window[left_c] < countT[left_c]:
                                have -=1

                        l += 1

        return res