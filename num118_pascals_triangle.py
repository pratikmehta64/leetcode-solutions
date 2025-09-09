from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        if numRows >= 1:
            triangle.append([1])
        if numRows > 1:
            triangle.append([1,1])
        for row_idx in range(2,numRows):
            row = [1]
            last_row = triangle[-1]
            
            for i, _ in enumerate(last_row):
                if i+1 < len(last_row):
                    row.append(last_row[i]+last_row[i+1])
            row.append(1)
            triangle.append(row)
        return triangle