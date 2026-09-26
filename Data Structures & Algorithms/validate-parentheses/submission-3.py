class Solution:
    def isValid(self, s: str) -> bool:
        # First we need to map openers to closers
        mapDict = {'(':')', '{':'}', '[':']'}
        parStack = []
        # Iterate through the string pushing to a stack if the char is an opener
        # if the char is a closer, first make sure stack isnt empty (aka possible openers exist) pop the top of the stack and if they dont match, return False
        # after loop, make sure stack isnt empty (openers are left)
        # return true outside of the loop
        for i in range(len(s)):
            if s[i] in mapDict:
                parStack.append(s[i])
                print(parStack)
            else:
                if len(parStack) == 0:
                    return False
                else:
                    top = parStack.pop()
                    if mapDict[top] != s[i]:
                        return False
        if len(parStack) == 0:
            return True
        else:
            return False
