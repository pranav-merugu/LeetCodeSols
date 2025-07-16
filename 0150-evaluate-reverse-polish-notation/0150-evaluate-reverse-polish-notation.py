class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = [] #3, 3
        operands = {"*", "/", "+", "-"}
        for token in tokens:
            if token in operands:
                result = 0
                num2 = int(stack.pop()) #1
                num1 = int(stack.pop()) #2
                if token == "*":
                    result += (num1 * num2)
                elif token == "+":
                    result += (num1 + num2) #3
                elif token == "/":
                    result += (num1 / num2)
                else:
                    result += (num1 - num2)
                stack.append(result) #3
            else:
                stack.append(token)
        return int(stack.pop())
            


