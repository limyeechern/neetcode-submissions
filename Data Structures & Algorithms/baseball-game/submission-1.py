class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        def plus():
            a = stack[-1]
            b = stack[-2]
            stack.append(a + b)
        
        def invalidate():
            stack.pop()
        
        def double():
            a = stack[-1]
            stack.append(a * 2)

        for op in operations:
            match op:
                case "+":
                    plus()
                case "C":
                    invalidate()
                case "D":
                    double() 
                case _:
                    stack.append(int(op))

        return sum(stack)


        