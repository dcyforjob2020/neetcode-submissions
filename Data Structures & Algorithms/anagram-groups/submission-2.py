class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)

        for s in strs:
            sList = str(sorted(s))
            group = map[sList]
            group.append(s)

        return list(map.values())