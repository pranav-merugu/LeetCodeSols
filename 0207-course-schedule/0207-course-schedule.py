from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
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
        
        print(in_degree)
        
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
        
