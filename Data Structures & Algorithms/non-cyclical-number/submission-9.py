class Solution:
    def isHappy(self, n: int) -> bool:
        memo = set() # Memo of past sums
        squareSum = 0
        while n not in memo:
            memo.add(n)
            digits = [int(d) for d in str(n)]
            for d in digits:
                squareSum += (d * d)
            # print(digits)
            # print("Sum: ", squareSum)
            if squareSum == 1:
                return True
            n = squareSum
            squareSum = 0
        return False

