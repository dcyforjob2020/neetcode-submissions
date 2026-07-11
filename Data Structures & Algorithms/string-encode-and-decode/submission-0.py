class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        # loop through strs
        for s in strs:
            # put length of str and # before the s
            res += str(len(s)) + "#" + s

        return res

    def decode(self, s: str) -> List[str]:
        res = []

        # initialize index
        i = 0

        # loop through s
        while i < len(s):
            element_len = 0

            # get the length of element
            while s[i] != "#":
                element_len = element_len * 10 + int(s[i])
                i += 1
            
            # skip the delimeter
            i += 1

            # get the element
            res.append(s[i: i + element_len])

            i += element_len

        return res