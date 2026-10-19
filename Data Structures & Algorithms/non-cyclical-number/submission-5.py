class Solution:
    def isHappy(self, n: int) -> bool:
        memo = [] # Memo of past sums
        squareSum = 0
        while squareSum != 1:
            digits = [int(d) for d in str(n)]
            for d in digits:
                squareSum += d * d
            memo.append(squareSum)
            print(digits)
            print(squareSum)
            n = squareSum
            if squareSum in memo and squareSum != 1:
                return False
        return True

