class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for op in operations:
            if op.isdigit() or (op[0] == '-' and op[1:].isdigit()):
                record.append(int(op))
            elif op == 'D':
                record.append(record[-1] * 2)
            elif op == '+':
                record.append(record[-1] + record[-2])
            else:
                record.pop()
        
        return sum(record)
