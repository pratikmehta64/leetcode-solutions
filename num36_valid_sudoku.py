class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        valid = True
        
        def count_dots(row):
            return len(filter(lambda x: x == ".", row))
        
        def valid_row(row):
            if len(set(row)) + count_dots(row)-1 == len(row):
                return True
            else:
                return False
        
        def validate_all_rows(board):    
            for i in range(9):
                if not valid_row(board[i]):
                    return False
            
        valid = validate_all_rows(board)
        if valid == False:
            return False
        board = map(list, zip(*board))
        valid = validate_all_rows(board)
        if valid == False:
            return False
        
        for row_idx in range(0,7,3):
            for col_idx in range(0,7,3):
                box_row = []
                box_row.extend(board[row_idx][col_idx:col_idx+3])
                box_row.extend(board[row_idx+1][col_idx:col_idx+3])
                box_row.extend(board[row_idx+2][col_idx:col_idx+3])
                valid = valid_row(box_row)
                if valid == False:
                    return False
        return True