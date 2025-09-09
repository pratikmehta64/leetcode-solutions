from typing import List
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        for _ in range(rowIndex):
            new_row = [1] * (len(row) + 1)
            for j in range(1,len(row)):
                new_row[j] = row[j-1] + row[j]
            row = new_row
        return row