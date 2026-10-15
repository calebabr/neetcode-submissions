class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {'+', '-', '*', '/'}
        nums = []
        for t in tokens:
            if t not in operators:
                nums.append(t)
            else:
                second = nums.pop()
                first = nums.pop()
                if t == '+':
                    nums.append(int(first) + int(second))
                elif t == '*':
                    nums.append(int(first) * int(second))
                elif t == '-':
                    nums.append(int(first) - int(second))
                else:
                    nums.append(int(first) / int(second))
        return int(nums[-1])
