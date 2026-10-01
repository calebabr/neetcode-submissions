class Solution:
    def isValid(self, s: str) -> bool:
        openDict = {'(':')', '[':']', '{':'}'}
        openStack = []
        for char in s:
            if char in openDict:
                openStack.append(char)
            else:
                if len(openStack) == 0:
                    return False
                curr = openStack.pop()
                if openDict[curr] != char:
                    return False
        if len(openStack) != 0:
            return False
        return True