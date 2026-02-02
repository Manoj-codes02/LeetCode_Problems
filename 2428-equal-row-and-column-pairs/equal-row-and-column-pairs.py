from collections import Counter

class Solution(object):
    def equalPairs(self, grid):
        n = len(grid)

        row_count = Counter(tuple(row) for row in grid)

        ans = 0

        for c in range(n):
            col = tuple(grid[r][c] for r in range(n))
            ans += row_count[col]

        return ans
