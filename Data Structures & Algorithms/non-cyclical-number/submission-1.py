class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        sum = 0

        for c in str(n):
            sum += int(c) ** 2

        while sum not in seen:
            if sum == 1:
                return True

            seen.add(sum)

            new_sum = 0

            for c in str(sum):
                new_sum += int(c) ** 2

            sum = new_sum

        return False