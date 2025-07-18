class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = []
        for i in range(len(position)):
            pairs.append([position[i], speed[i]])
        pairs.sort(reverse = True)
        stack = []
        for pair in pairs:
            stack.append((target - pair[0])/pair[1])
            if len(stack) >= 2:
                if stack[-1] <= stack[-2]:
                    stack.pop()
        return len(stack)
