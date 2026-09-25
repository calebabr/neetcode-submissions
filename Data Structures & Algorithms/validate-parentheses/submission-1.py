class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                stack.append(s[i])
            if s[i] == ')':
                if not stack:
                    return False
                recent = stack.pop()
                if recent != '(':
                    return False
            if s[i] == '}':
                if not stack:
                    return False
                recent = stack.pop()
                if recent != '{':
                    return False
            if s[i] == ']':
                if not stack:
                    return False
                recent = stack.pop()
                if recent != '[':
                    return False
        return not stack
        