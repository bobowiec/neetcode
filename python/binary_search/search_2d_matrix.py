class Solution:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        left, right = 0, ROWS * COLS - 1
        while left <= right:
            mid = (left + right) // 2
            row, col = mid // COLS, mid % COLS
            if target > matrix[row][col]:
                left = mid + 1
            elif target < matrix[row][col]:
                right = mid - 1
            else:
                return True
        return False

    def searchMatrixTwoPasses(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        top, bottom = 0, m - 1
        while top <= bottom:
            row = (top + bottom) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bottom = row - 1
            else:
                break
        
        if not (top <= bottom):
            return False
        
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            if target > matrix[row][mid]:
                left = mid + 1
            elif target < matrix[row][mid]:
                right = mid - 1
            else:
                return True

        return False

    # Time complexity: O(log(m*n)), Space complexity: O(m)
    def searchMatrix2(self, matrix: List[List[int]], target: int) -> bool:
        column_zero = [row[0] for row in matrix]
        
        # find the row where a target can be
        m = len(column_zero)
        row = m - 1
        left, right = 0, m - 1
        while left <= right:
            mid = (left + right) // 2
            if column_zero[mid] > target:
                if mid - 1 > 0 and column_zero[mid - 1] < target:
                    row = mid - 1
                    break
                right = mid - 1
            elif column_zero[mid] < target:
                if mid + 1 < m and column_zero[mid + 1] > target:
                    row = mid
                    break    
                left = mid + 1
            else:
                return True
        
        if self.binarySearch(matrix[row], target) != -1:
            return True
        
        return False

    # Time complexity: O(M * logN), Space complexity: O(1)
    def searchMatrixNotOpt(self, matrix: List[List[int]], target: int) -> bool:
        for row in range(len(matrix)):
            if self.binarySearch(matrix[row], target) != -1:
                return True
        return False

    def binarySearch(self, arr: List[int], target: int) -> int:
        l, r = 0, len(arr) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if arr[mid] > target:
                r = mid - 1
            elif arr[mid] < target:
                l = mid + 1
            else:
                return mid
        return -1
    
    def searchMatrixBF(self, matrix: List[List[int]], target: int) -> bool:
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == target:
                    return True
        return False
