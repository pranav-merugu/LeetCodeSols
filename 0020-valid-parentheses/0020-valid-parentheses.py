class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        checkParentheses = {"]": "[", "}":"{", ")": "("}
        for c in s:
            if c in checkParentheses:
                if stack and stack[-1] == checkParentheses[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return False if stack else True
        