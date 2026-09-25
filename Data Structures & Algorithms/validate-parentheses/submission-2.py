class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {'(':')', '{':'}', '[':']'}
        for i in range(len(s)):
            if s[i] in match:
                stack.append(s[i])
            else:
                if not stack:
                    return False
                recent = stack.pop()
                if match[recent] != s[i]:
                    return False
        return not stack
        