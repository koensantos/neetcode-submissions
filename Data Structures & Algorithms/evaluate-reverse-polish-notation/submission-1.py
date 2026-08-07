class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in range(0, len(tokens)):
            if tokens[i] == "+":
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(a + b)
            elif tokens[i] == "-":
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(b - a)
            elif tokens[i] == "*":
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(a * b)
            elif tokens[i] == "/":
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(int(b / a))
            else:
                stack.append(tokens[i])
        return int(stack[0])