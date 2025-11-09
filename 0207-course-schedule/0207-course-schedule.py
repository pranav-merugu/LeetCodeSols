from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = defaultdict(list)
        in_degree = [0] * numCourses
        for course, prereq in prerequisites:
            courses[prereq].append(course)
            in_degree[course] += 1
        
        queue = deque([])
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)
        
        completed = 0
        while queue:
            cur = queue.popleft()
            completed += 1

            for node in courses[cur]:
                in_degree[node] -= 1
                if in_degree[node] == 0:
                    queue.append(node)
        
        return completed == numCourses
        '''

        courses = defaultdict(list)
        for course, prereq in prerequisites:
            courses[course].append(prereq)
        
        visited = set()
        def dfs(course):
            if courses[course] == []:
                return True
            
            if course in visited:
                return False
            
            visited.add(course)
            for prereq in courses[course]:
                if not dfs(prereq):
                    return False
            
            courses[course] = []
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True
        '''
