class Solution(object):
    def longest_increasing_path(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        # make sure the matrix is valid
        if not matrix:
            return 0
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        # initialize cache
        m = len(matrix)
        n = len(matrix[0])
        cache = [[0 for _ in row] for row in matrix]

        # calculate path lengths
        for i in range(m):
            for j in range(n):
                self.calculate_path_length(matrix, i, j, cache)

        # find the maximum length
        return max([max(row) for row in cache])

    def calculate_path_length(self, matrix, i, j, cache):
        if cache[i][j] == 0:
            up, left, right, down = 0, 0, 0, 0
            if i - 1 >= 0 and matrix[i - 1][j] < matrix[i][j]:
                up = self.calculate_path_length(matrix, i - 1, j, cache)
            if j - 1 >= 0 and matrix[i][j - 1] < matrix[i][j]:
                left = self.calculate_path_length(matrix, i, j - 1, cache)
            if j + 1 < len(matrix[0]) and matrix[i][j + 1] < matrix[i][j]:
                right = self.calculate_path_length(matrix, i, j + 1, cache)
            if i + 1 < len(matrix) and matrix[i + 1][j] < matrix[i][j]:
                down = self.calculate_path_length(matrix, i + 1, j, cache)

            cache[i][j] = max([up, left, right, down]) + 1

        return cache[i][j]

Solution().longest_increasing_path([[3, 4, 5], [3, 2, 6], [2, 2, 1]])
