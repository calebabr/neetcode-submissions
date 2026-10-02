class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = 0
        record = [] # only add numbers to this
        for op in operations:
            if op != '+' and op != 'C' and op != 'D':
                record.append(int(op))
            elif op == 'D':
                record.append(2 * record[-1])
            elif op == 'C':
                record.pop()
            else:
                record.append(record[-1] + record[-2])
        # for num in record:
            # score += num
        return sum(record)