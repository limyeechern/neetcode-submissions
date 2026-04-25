class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = path.split("/")
        stack = []
        print(paths)
        for p in paths:
            if p == "..":
                if stack:
                    stack.pop()
            elif p != "" and p != ".":
                stack.append(p)
        
        print(stack)
        return "/" + "/".join(stack)
