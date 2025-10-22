"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        directory = {}
        for e in employees:
            directory[e.id] = e

        queue = [id] 
        res = 0
        visited = set()

        while queue:
            cur = queue.pop(0)
            res += directory[cur].importance
            visited.add(cur)
            for sub in directory[cur].subordinates:
                if sub not in visited:
                    queue.append(sub)
            
        return res

                



        