class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = 0
        record = []
        for op in operations:
            if op != 'D' and op != 'C' and op != '+':
                record.append(int(op))
            elif op == 'D':
                record.append(2 * int(record[-1]))
            elif op == 'C':
                record.pop()
            else:
                record.append(record[len(record) - 1] + record[len(record) - 2])
        for i in range(len(record)):
            score += record[i]
        return score
