# MEDIUM
# Time: O(mn) Space: O(1)
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS, COLS = len(matrix), len(matrix[0])
        row_zero = False
        
        # determines which rows/columns need to be converted
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    # converts top row for later column conversion
                    matrix[0][c] = 0
                    
                    # converts left column for later row conversion
                    # skips first row to avoid row/column stacking
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        row_zero = True
        
        # converts most indices
        # cant convert all or values may change
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        
        # converts left column
        # must do this before converting first row or matrix[0][0] may change values
        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0
        
        # converts first row
        if row_zero:
            for c in range(COLS):
                matrix[0][c] = 0