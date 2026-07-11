class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sList = list(s)
        sList.sort()
        tList = list(t)
        tList.sort()

        if len(sList) != len(tList):
            return False

        for i in range(len(sList)):
            if sList[i] != tList[i]:
                return False

        return True