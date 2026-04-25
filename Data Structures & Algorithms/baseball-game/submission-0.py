class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        def isOperation(op):
            return op == "+" or op == "C" or op == "D"
        
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
            print(stack)
            if isOperation(op):
                match op:
                    case "+":
                        plus()
                    case "C":
                        invalidate()
                    case "D":
                        double() 
            else:
                stack.append(int(op))

        ans = 0
        for i in stack:
            ans += i
        return ans


        