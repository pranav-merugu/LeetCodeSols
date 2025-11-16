class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj = defaultdict(set)
        in_degree = defaultdict(int)
        letters = set("".join(words))
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]

            ptr = 0
            while ptr < len(word1) and ptr < len(word2) and word1[ptr] == word2[ptr]:
                ptr += 1
            
            if ptr < len(word1) and ptr == len(word2): #Ex: abc vs ab which is an invalid ordering
                return ""
            
            if ptr == len(word1) or ptr == len(word2):
                continue
            
            a = word1[ptr]
            b = word2[ptr]
            if b not in adj[a]:
                adj[a].add(b)
                in_degree[b] += 1
        

        min_heap = []
        for char in letters:
            if in_degree[char] == 0:
                heapq.heappush(min_heap, char)

        print(min_heap)

        res = ""
        while min_heap:
            cur = heapq.heappop(min_heap)
            res += cur
            for char in adj[cur]:
                in_degree[char] -= 1
                if in_degree[char] == 0:
                    heapq.heappush(min_heap, char)
        
        if len(res) != len(letters):
            return ""
        
        return res