class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []

        adj = [[] for i in range(numCourses)]

        indegree = [0] * numCourses

        for course, prerequisite in prerequisites:
            indegree[course] += 1

            adj[prerequisite].append(course)

        q = []

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        for course in q:
            res.append(course)

            for edge in adj[course]:
                indegree[edge] -= 1

                if indegree[edge] == 0:
                    q.append(edge)

        return res if len(res) == numCourses else []