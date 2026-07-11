class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        sLower = s.lower()

        while l < r:
            if not sLower[l].isalnum():
                l += 1
                continue
            if not sLower[r].isalnum():
                r -= 1
                continue
            if sLower[l] != sLower[r]:
                return False
            l += 1
            r -= 1

        return True