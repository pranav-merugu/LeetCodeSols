class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n 
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX != rootY:
            # Attach smaller tree under larger tree
            if self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            elif self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        emailToAcc = {}

        for i, a in enumerate(accounts):
            for email in a[1:]:
                if email in emailToAcc:
                    uf.union(i, emailToAcc[email])
                else:
                    emailToAcc[email] = i
        
        emailGroup = defaultdict(list)
        for e, i in emailToAcc.items():
            owner = uf.find(i)
            emailGroup[owner].append(e)
        
        res = []
        for i, emails in emailGroup.items():
            res.append([accounts[i][0]] + sorted(emailGroup[i]))
        
        return res