# MEDIUM
# Time: O(n) Space: O(1)
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        left, right = 0, len(matrix[0]) - 1
        top, bottom = 0, len(matrix) - 1
    
        while left < right and top < bottom:
            
            for i in range(0, right - left):
                # first replacement
                curr = matrix[top][left + i]
                temp = matrix[top + i][right]
                matrix[top + i][right] = curr
                
                # second replacement
                curr = temp
                temp = matrix[bottom][right - i]
                matrix[bottom][right - i] = curr
                
                # third replacment
                curr = temp
                temp = matrix[bottom - i][left]
                matrix[bottom - i][left] = curr
                
                # fourth replacement
                curr = temp
                temp = matrix[top][left + i]
                matrix[top][left + i] = curr
            
            # increment pointers
            left += 1
            right -= 1
            top += 1
            bottom -= 1
                
        return matrix
                