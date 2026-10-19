class Solution:
    def isHappy(self, n: int) -> bool:
        memo = {} # Memo of past sums
        squareSum = 0
        while n != 1:
            digits = [int(d) for d in str(n)]
            for d in digits:
                squareSum += (d * d)
            # print(digits)
            # print("Sum: ", squareSum)
            if squareSum in memo and squareSum != 1:
                return False
            memo[squareSum] = squareSum
            n = squareSum
        return True

