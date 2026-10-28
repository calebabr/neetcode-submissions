class Solution:
    def isValid(self, s: str) -> bool:
        openDict = {'(':')', '{':'}', '[':']'}
        openStack = []
        for char in s:
            if char in openDict:
                openStack.append(char)
            else:
                top = openStack.pop()
                if openDict[top] == char:
                    continue
                else:
                    return False
        return len(openStack) == 0