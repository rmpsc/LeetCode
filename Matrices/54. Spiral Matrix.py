# MEDIUM
# Time: O(mn) Space: O(n)
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)
        spiral = []
        
        while left < right and top < bottom:
            
            # append top of matrix
            for i in range(left, right):
                spiral.append(matrix[top][i])
            top += 1
            
            # append right of matrix
            for i in range(top, bottom):
                spiral.append(matrix[i][right - 1])
            right -= 1
               
            # needed in case matrix only has 1 row or 1 column
            if not (left < right and top < bottom):
                break
                
            # append bottom of matrix
            for i in range(right - 1, left - 1, -1):
                spiral.append(matrix[bottom - 1][i])
            bottom -= 1
            
            # append left of matrix
            for i in range(bottom - 1, top - 1, -1):
                spiral.append(matrix[i][left])
            left += 1
            
        return spiral
        