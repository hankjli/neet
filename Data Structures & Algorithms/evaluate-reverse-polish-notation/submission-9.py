class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        def perform_operation(op, a, b):
            if op == "+":
                return a + b
            elif op == "-":
                return a - b
            elif op == "*":
                return a * b
            else:
                return int(a / b)

        operators = set(["+", "-", "*", "/"])
        
        operands = []

        for token in tokens:
            if token not in operators:
                operands.append(token)
            
            else: # operator
                b = int(operands.pop())
                a = int(operands.pop())
                res = perform_operation(token, a, b)

                operands.append(res)

        return int(operands.pop())
        