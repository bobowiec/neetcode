class Solution:

    # Time Complexity: O(n), Space Complexity: O(n)
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        operators = {'+', '-', '*', '/'}

        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                    # Use int() to truncate towards zero
                    stack.append(int(a / b))

        return stack[0]