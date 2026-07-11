class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for s in strs:
            arr = [0 for _ in range(26)]

            for c in s:
                arr[ord(c) - ord("a")] += 1 

            t = tuple(arr)

            # anagrams[t] = anagrams.get(t,[])
            anagrams[t].append(s)


        return list(anagrams.values())