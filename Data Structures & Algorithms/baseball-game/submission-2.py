class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = 0
        record = [] # only add numbers to this
        for op in operations:
            if op != '+' and op != 'C' and op == 'D':
                record.append(int(op))
            elif op == '+':
                record.append(record[len(record) - 1] + record[len(record) - 2])
            elif op == 'D':
                record.append(2 * record[-1])
            else:
                record.pop()
        for num in record:
            score += num
        return score