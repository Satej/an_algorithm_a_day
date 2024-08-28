class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        row, col = self.find_empty_cell(board)

        if row == -1:
            return True

        for num in range(1, 10):
            if self.is_safe(board, row, col, num):
                board[row][col] = str(num)
                if self.solveSudoku(board):
                    return True
                board[row][col] = '.'

        return False
    
    def find_empty_cell(self, grid):
        for i in range(9):
            for j in range(9):
                if grid[i][j] == '.':
                    return (i, j)
        
        return (-1, -1)
    
    def is_safe(self, grid, row, col, num):
        # Check if the number is already in the current row
        for i in range(9):
            if grid[row][i] == str(num):
                return False
        
        # Check if the number is already in the current column
        for i in range(9):
            if grid[i][col] == str(num):
                return False
        
        # Check if the number is already in the current 3x3 box
        start_row = row - row % 3
        start_col = col - col % 3

        for i in range(3):
            for j in range(3):
                if grid[start_row + i][start_col + j] == str(num):
                    return False
        
        return True
