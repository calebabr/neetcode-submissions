class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        alphabet = []
        answer = ""
        while(columnNumber > 0):
            digit = (columnNumber - 1) % 26
            answer = chr(digit + 65) + answer
            columnNumber = (columnNumber - 1) // 26
        return answer
        