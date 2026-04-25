class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        def left(op):
            return op == "(" or op == "[" or op == "{"

        for op in s:
            match op:
                case "(":
                    stack.append(op)
        
                case "[":
                    stack.append(op)
        
                case "{":
                    stack.append(op)
        
                case ")":
                    if not stack:
                        return False
                    topMost = stack[-1]
                    if left(topMost) and topMost != "(":
                        return False
                    stack.pop()
        
                case "]":
                    if not stack:
                        return False
                    topMost = stack[-1]
                    if left(topMost) and topMost != "[":
                        return False
                    stack.pop()

                case "}":
                    if not stack:
                        return False
                    topMost = stack[-1]
                    if left(topMost) and topMost != "{":
                        return False
                    stack.pop()
        
        return len(stack) == 0