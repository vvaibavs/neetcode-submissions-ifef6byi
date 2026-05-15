class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ["+", "-", "/", "*"]
        operators = set(operators)
        stack = []
        for t in tokens:
            if t not in operators:
                stack.append(int(t))
            else:
                second = stack.pop()
                first = stack.pop()
                result = str(first) + str(t) + str(second)
                result = eval(result)
                stack.append(int(result)) 
        print(stack)
        return stack.pop()