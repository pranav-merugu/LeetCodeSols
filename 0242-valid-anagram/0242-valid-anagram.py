class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars = {}
        for char in s:
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 1
        
        for char in t:
            if char in chars:
                chars[char] -= 1
            else:
                return False
        
        for value in chars.values():
            if value != 0:
                return False

        return True
        