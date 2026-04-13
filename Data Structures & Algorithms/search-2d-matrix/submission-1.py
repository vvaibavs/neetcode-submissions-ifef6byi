class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1
        
        midy = bottom//2
        midx = right//2
        while top <= bottom:
            print(midy)
            if matrix[midy][left] <= target and matrix[midy][right] >= target:
                while left <= right:
                    if matrix[midy][midx] == target:
                        return True
                    elif matrix[midy][midx] < target:
                        left = midx + 1
                    else: 
                        right = midx - 1
                    midx = left+(right-left)//2
            elif matrix[midy][left] > target:
                bottom = midy-1
            else:
                top = midy+1
            midy = top + (bottom-top)//2
        
        return False