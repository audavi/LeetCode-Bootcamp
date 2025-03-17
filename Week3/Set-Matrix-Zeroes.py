class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        arr = []

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    arr.append([i, j])

        for a, b in arr:
            for row in range(n):
                matrix[a][row] = 0
            for col in range(m):
                matrix[col][b] = 0
