from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
        Solution 1: Kahn's Algorithm

        prereqs = defaultdict(list)
        nodes = set()
        maxCourse = -1
        for postreq, prereq in prerequisites:
            prereqs[prereq].append(postreq)
            nodes.add(prereq)
            nodes.add(postreq)
            maxCourse = max(maxCourse, max(prereq, postreq))
        
        in_degree = [0] * (maxCourse + 1)
        for postreq, prereq in prerequisites:
            in_degree[postreq] += 1
        
        queue = deque([])
        for node, degree in enumerate(in_degree):
            if degree == 0 and node in nodes:
                queue.append(node)
        
        res = []
        while queue:
            cur = queue.popleft()
            res.append(cur)
            for node in prereqs[cur]:
                in_degree[node] -= 1
                if in_degree[node] == 0:
                    queue.append(node)
        
        if len(res) != len(nodes):
            return False
        else:
            return True
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
        
