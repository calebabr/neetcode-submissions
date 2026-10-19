class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {'+', '-', '*', '/'}
        nums = []
        for t in tokens:
            if t not in operators:
                nums.append(t)
            else:
                second = int(nums.pop())
                first = int(nums.pop())
                if t == '+':
                    nums.append(first + second)
                elif t == '*':
                    nums.append(first * second)
                elif t == '-':
                    nums.append(first - second)
                else:
                    nums.append(firs / second)
        return int(nums[-1])
