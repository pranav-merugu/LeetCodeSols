class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)
        for stri in strs:
            key = [0] * 26
            for char in stri:
                key[ord(char) - ord('a')] += 1

            seen[tuple(key)].append(stri)
        
        return list(seen.values())
        