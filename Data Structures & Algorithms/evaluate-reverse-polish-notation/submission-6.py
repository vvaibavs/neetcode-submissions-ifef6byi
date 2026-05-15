class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ["+", "-", "/", "*"]
        operators = set(operators)
        stack = []
        for t in tokens:
            if t not in operators:
                stack.append(int(t))
            elif t == "+":
                stack.append(stack.pop() + stack.pop())
            elif t == "-":
                second = stack.pop()
                first = stack.pop()
                stack.append(first - second)
            elif t == "*":
                stack.append(stack.pop() * stack.pop())
            elif t == "/":
                second = stack.pop()
                first = stack.pop()
                stack.append(int(first/second))
        return stack.pop()