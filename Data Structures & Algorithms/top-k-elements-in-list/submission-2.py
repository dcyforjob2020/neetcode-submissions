class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freq = defaultdict(int)

        for num in nums:
            num_freq[num] += 1

        freq_num = []

        for key, val in num_freq.items():
            freq_num.append((val, key))

        heapq.heapify(freq_num)

        return [key for val, key in heapq.nlargest(k, freq_num)]