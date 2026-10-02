class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = 0
        record = [] # only add numbers to this
        for op in operations:
            if op != '+' and op != 'C' and op != 'D':
                record.append(int(op))
            elif op == 'D':
                record.append(2 * int(record[-1]))
            elif op == 'C':
                record.pop()
            else:
                record.append(record[len(record) - 1] + record[len(record) - 2])
        for num in record:
            score += num
        return score