class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {n : [] for n in range(numCourses)}

        for course, pre in prerequisites:
            preMap[course].append(pre)

        visited = set()

        def dfs(course):
            if preMap[course] == []:
                return True
            if course in visited:
                return False
            visited.add(course)
            for pre in preMap[course]:
                if not dfs(pre):
                    return False
            preMap[course] = []
            return True

        for course, pre in prerequisites:
            dfs(course)

        print(preMap)
        for k,v in preMap.items():
            if len(v) >= 1:
                return False
        return True
