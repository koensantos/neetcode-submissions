class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        
        for s in operations:
            if s == "+":
                num1, num2 = int(stack[-1]), int(stack[-2])
                stack.append(num1 + num2)
            elif s == "C":
                stack.pop()
            elif s == "D":
                stack.append(int(stack[-1]) * 2)
            else:
                stack.append(int(s))
        
        #[1,2,5,10]
        #18
        return sum(stack)