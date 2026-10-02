class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        sumTotal = 0
        if len(tokens) == 1:
            return int(tokens[0])
        for i in range(len(tokens)):
            if tokens[i] == '+':
                sumTotal = int(stack.pop()) + int(stack.pop())
                stack.append(sumTotal)
            elif tokens[i] == '*':
                sumTotal = int(stack.pop()) * int(stack.pop())
                stack.append(sumTotal)
            elif tokens[i] == '-':
                numOne = int(stack.pop())
                numTwo = int(stack.pop())
                sumTotal = numTwo - numOne
                stack.append(sumTotal)
            elif tokens[i] == '/':
                numOne = int(stack.pop())
                numTwo = int(stack.pop())
                sumTotal = int(numTwo / numOne)
                stack.append(sumTotal)
            else:
                stack.append(tokens[i])
        return stack.pop()