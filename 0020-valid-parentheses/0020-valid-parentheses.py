class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if (c == "{" or c == "(" or c == "["):
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                else:
                    check = stack.pop()
                    if (check == "{" and c == "}"):
                        continue
                    elif (check == "(" and c == ")"):
                        continue
                    elif (check == "[" and c == "]"):
                        continue
                    else:
                        return False
        if len(stack) == 0:
            return True
        else:
            return False
                
        