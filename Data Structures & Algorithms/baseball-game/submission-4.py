class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for i in range(len(operations)):
            if operations[i] == '+':
                record.append(int(record[-2]) + int(record[-1])) #
            elif operations[i] == 'C':
                record.pop(-1)
            elif operations[i] == 'D':
                record.append(int(record[-1]) * 2)
            else:
                record.append(int(operations[i]))
        return sum(record)