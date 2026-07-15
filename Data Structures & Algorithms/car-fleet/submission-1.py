class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        result = 0

        n = len(position)

        p_s = []

        for i in range(n):
            p_s.append((position[i], speed[i]))

        p_s.sort(reverse=True)

        max_duration = 0

        for p, s in p_s:
            duration = (target - p) / s

            if duration > max_duration:
                result += 1
                max_duration = duration

        return result
            