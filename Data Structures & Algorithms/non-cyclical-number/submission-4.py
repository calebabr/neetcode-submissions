class Solution:
    def isHappy(self, n: int) -> bool:
        memo = []
        squareSum = 0
        while squareSum != 1:
            digits = [int(d) for d in str(n)]
            for d in digits:
                squareSum += d * d
            memo.append(squareSum)
            print(digits)
            print(squareSum)
            n = squareSum
            if squareSum != 1 or squareSum not in memo:
                return False
        return True

