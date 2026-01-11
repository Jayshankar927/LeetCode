'''Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.'''

def maximalRectangle(matrix):
    if not matrix:
        return 0

    n, m = len(matrix), len(matrix[0])
    heights = [0]*m
    max_area = 0

    for row in matrix:
        # Build histogram
        for i in range(m):
            if row[i] == "1":
                heights[i] += 1
            else:
                heights[i] = 0

        # Largest rectangle in histogram
        stack = []
        for i in range(m+1):
            cur = heights[i] if i < m else 0
            while stack and cur < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, h * w)
            stack.append(i)

    return max_area
