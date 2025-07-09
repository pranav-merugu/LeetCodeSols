class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        for i, c in enumerate(s):
            if c == ")":
                if stack and stack[-1][0] == "(":
                    stack.pop()
                else:
                    stack.append((c, i))
            elif c == "(":
                stack.append((c, i))
        
        print(stack)
        
        pos = {}
        for t in stack:
            pos[t[1]] = t[0]
        
        res = ""
        for i, c in enumerate(s):
            if i not in pos:
                res += c

        return res

        