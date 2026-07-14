class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0 for _ in range(len(temperatures))]

        stack = []

        for i, temperature in enumerate(temperatures):
            while stack and stack[-1][0] < temperature:
                val, index = stack.pop()
                
                result[index] = i - index

            stack.append((temperature, i))

        return result