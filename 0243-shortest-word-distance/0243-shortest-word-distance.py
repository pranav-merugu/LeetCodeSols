class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        index1 = -1
        index2 = -1
        minDistance = 30001
        for idx, word in enumerate(wordsDict):
            if word == word1:
                index1 = idx
            elif word == word2:
                index2 = idx
            
            if index1 != -1 and index2 != -1:
                minDistance = min(abs(index1 - index2), minDistance)
        
        return minDistance