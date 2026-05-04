class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereqMap = {i:[] for i in range(numCourses)}
        for course, pre in prerequisites:
            prereqMap[course].append(pre)

        visited = set()
        done = set()
        path = []

        def dfs(course):
            if course in visited:
                return False # cycle
            if course in done:
                return True

            visited.add(course)
            for pre in prereqMap[course]:
                if not dfs(pre):
                    return False
            visited.remove(course)
            done.add(course)
            path.append(course)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return path

