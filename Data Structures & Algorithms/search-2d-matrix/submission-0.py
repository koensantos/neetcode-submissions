class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l1 = 0
        r1 = len(matrix) - 1
        row = []
        while l1 <= r1:
            m1 = l1 + (r1 - l1) // 2
            if target >= matrix[m1][0] and target <= matrix[m1][-1]:
                row = matrix[m1]
                break
            elif target >= matrix[m1][-1]:
                l1 = m1 + 1
            else:
                r1 = m1 - 1
        l2 = 0
        r2 = len(row) - 1
        while l2 <= r2:
            m2 = l2 + (r2 - l2) // 2
            if target == row[m2]:
                return True
            elif target > row[m2]:
                l2 = m2 + 1
            else:
                r2 = m2 - 1
        return False