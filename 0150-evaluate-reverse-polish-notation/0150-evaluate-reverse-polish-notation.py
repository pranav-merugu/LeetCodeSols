from collections import deque

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = deque()
        for token in tokens:
            if token != "+" and token != "-" and token != "*" and token != "/":
                operands.append(int(token))
            else:
                operand1 = operands.pop()
                operand2 = operands.pop()
                res = 0
                if token == "+":
                    res = operand2 + operand1
                elif token == "-":
                    res = operand2 - operand1
                elif token == "*":
                    res = operand2 * operand1
                else:
                    res = int(operand2 / operand1)
                operands.append(res)
        
        if len(operands) == 2:
            return operands.pop() + operands.pop()
        else:
            return operands.pop()