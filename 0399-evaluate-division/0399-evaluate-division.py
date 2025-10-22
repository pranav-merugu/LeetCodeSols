class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        for i in range(len(equations)):
            graph[equations[i][0]][equations[i][1]] = values[i]
            graph[equations[i][1]][equations[i][0]] = 1 / values[i]
        
        def dfs(graph, source, target):
            if source not in graph or target not in graph:
                return -1.0
            if source == target:
                return 1.0

            stack = [(source, 1.0)]
            visited = set()
            
            while stack:
                cur, res = stack.pop()
                if cur == target:
                    return res
                visited.add(cur)
                for neighbor, val in graph[cur].items():
                    if neighbor not in visited:
                        stack.append((neighbor, res * val))
            return -1.0

        results = []
        for query in queries:
            results.append(dfs(graph, query[0], query[1]))
        return results
                
                    



            
        
        