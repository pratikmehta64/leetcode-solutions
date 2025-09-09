from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        targeted_rows = []
        targeted_cols = []
        def set_zero(matrix: List[List[int]], targeted_rows: List[int], targeted_cols: List[int]) -> List[List[int]]:
            m = len(matrix)
            n = len(matrix[0])
            for r_i, row in enumerate(matrix):
                if r_i in targeted_rows:
                    matrix[r_i] = [0]*n
                for c_i, ele in enumerate(row):
                    if c_i in targeted_cols:
                        matrix[r_i][c_i] = 0
            return matrix
        
        for r_i, row in enumerate(matrix):
            for c_i, ele in enumerate(row):
                if ele == 0:
                    targeted_rows.append(r_i)
                    targeted_cols.append(c_i)
        
        matrix = set_zero(matrix, targeted_rows, targeted_cols)
        