from collections import deque

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = deque()
        for token in tokens:
            if token == "+":
                operands.append(operands.pop() + operands.pop())
            elif token == "-":
                operand2 = operands.pop()
                operands.append(operands.pop() - operand2)
            elif token == "*":
                operands.append(operands.pop() * operands.pop())
            elif token == "/":
                operand2 = operands.pop()
                operands.append(int(operands.pop() / operand2))
            else:
                operands.append(int(token))
        
        return operands[0]