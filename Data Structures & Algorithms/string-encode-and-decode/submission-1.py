class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""

        for s in strs:
            result += str(len(s)) + "#" + s

        return result

    def decode(self, s: str) -> List[str]:
        result = []

        n = len(s)
        i = 0
        s_len = 0

        while i < n:
            print(i)
            if s[i].isdigit():
                s_len *= 10
                s_len += int(s[i])
                i += 1
            else:
                result.append(s[i + 1: i + s_len + 1])
                i += s_len + 1
                s_len = 0

        return result