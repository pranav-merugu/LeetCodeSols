from collections import defaultdict

class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.wordIdx = defaultdict(list)
        for idx, word in enumerate(wordsDict):
            self.wordIdx[word].append(idx)
        

    def shortest(self, word1: str, word2: str) -> int:
        idx1 = 0
        idx2 = 0
        minDistance = 30001
        while idx1 < len(self.wordIdx[word1]) and idx2 < len(self.wordIdx[word2]):
            minDistance = min(minDistance, abs(self.wordIdx[word1][idx1] - self.wordIdx[word2][idx2]))
            if idx1 + 1 < len(self.wordIdx[word1]) and abs(self.wordIdx[word1][idx1+1] - self.wordIdx[word2][idx2]) < minDistance:
                idx1 += 1
            elif idx2 + 1 < len(self.wordIdx[word2]) and abs(self.wordIdx[word1][idx1] - self.wordIdx[word2][idx2+1]) < minDistance:
                idx2 += 1
            else:
                idx1 += 1
                idx2 += 1
        
        return minDistance



# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)