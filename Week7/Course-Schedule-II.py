class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        after = [[] for i in range(numCourses)]
        indegree = [0] * numCourses

        for course, prereq in prerequisites:
            after[prereq].append(course)
            indegree[course] = indegree[course] + 1

        available = []
        for i in range(numCourses):
            if indegree[i] == 0:
                available.append(i)

        result = []
        while len(available) > 0:
            curr = available.pop()
            result.append(curr)

            for a in after[curr]:
                indegree[a] = indegree[a] - 1
                if indegree[a] == 0:
                    available.append(a)

        return [] if len(result) != numCourses else result
