class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch == "[" or ch == "(" or ch == "{":
                stack.append(ch)
            else:
                if len(stack)<=0:
                    return False
                ele = stack.pop()
                if ele == "[" and ch!="]" or ele == "{" and ch!="}" or  ele == "(" and ch!=")":
                    return False
        
        return len(stack) == 0