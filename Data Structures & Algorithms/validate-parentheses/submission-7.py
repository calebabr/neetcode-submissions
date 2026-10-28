class Solution:
    def isValid(self, s: str) -> bool:
        openDict = {'(':')', '{':'}', '[':']'}
        openStack = []
        for char in s:
            if char in openDict: # If its an opener, append to stack because its waiting
                openStack.append(char)
            else: # If its a closer
                if len(openStack) == 0: # if closer and no openers waiting, return False
                    return False

                top = openStack.pop() # otherwise, check if most recent opener matches
                if openDict[top] == char:
                    continue
                else:
                    return False
        return len(openStack) == 0 # Check if all openers have been matched