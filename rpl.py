class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for x in tokens:
            try:
                integer = int(x)
                stack.append(x)
            except ValueError:
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(str(int(eval(op1 + x + op2))))
        print(stack)
        return int(stack[0])
