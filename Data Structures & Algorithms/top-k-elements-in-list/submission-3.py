class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = Counter(nums)

        count = [[] for _ in range(len(nums) + 1)]

        for key, val in frequency.items():
            count[val].append(key)
            print(count)

        result = []
        for i in range(len(count) - 1, 0, -1):
            for j in range(len(count[i])):
                result.append(count[i][j])

                if len(result) == k:
                    return result
            