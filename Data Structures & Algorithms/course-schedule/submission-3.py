class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()
        cur = set()

        def dfs(i):
            res = False

            if not courses[i]:
                return False

            if i in cur:
                return True

            if i in visited:
                return False

            cur.add(i)

            for j in courses[i]:
                if dfs(j):
                    return True

            cur.remove(i)

            visited.add(i)

            return False

        courses = [[] for i in range(numCourses)]

        for course, prerequisite in prerequisites:
            courses[prerequisite].append(course)

        for i in range(numCourses):
            if dfs(i):
                return False

        return True