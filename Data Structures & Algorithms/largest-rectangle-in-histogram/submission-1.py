class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        result = 0

        stack = []

        for i, h in enumerate(heights):
            # print(stack)
            start_i = i

            while stack and stack[-1][1] > h:
                index, height = stack.pop()

                result = max(result, (i - index) * height)

                start_i = index

            stack.append((start_i, h))

        n = len(heights)

        for i, h in stack:
            result = max(result, (n - i) * h)

        return result

            