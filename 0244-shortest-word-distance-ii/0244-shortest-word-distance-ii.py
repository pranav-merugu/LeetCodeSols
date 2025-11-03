from collections import defaultdict

class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.wordIdx = defaultdict(list)
        for idx, word in enumerate(wordsDict):
            self.wordIdx[word].append(idx)
        

    def shortest(self, word1: str, word2: str) -> int:
        idx1, idx2 = 0, 0
        indexes1 = self.wordIdx[word1]
        indexes2 = self.wordIdx[word2]
        minDistance = float('inf')
        while idx1 < len(indexes1) and idx2 < len(indexes2):
            minDistance = min(minDistance, abs(indexes1[idx1] - indexes2[idx2]))
            if indexes1[idx1] <= indexes2[idx2]:
                idx1 += 1
            else:
                idx2 += 1
        
        return minDistance



# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)