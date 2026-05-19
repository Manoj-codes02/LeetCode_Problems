class Solution(object):
    def isMatch(self, s, p):

        dp = {}

        def dfs(i, j):

            if (i, j) in dp:
                return dp[(i, j)]

            if i == len(s) and j == len(p):
                return True

            if j == len(p):
                return False

            match = i < len(s) and (
                s[i] == p[j] or p[j] == "."
            )

            if j + 1 < len(p) and p[j + 1] == "*":

                # choice 1 -> ignore
                ignore = dfs(i, j + 2)

                # choice 2 -> use character
                use = match and dfs(i + 1, j)

                dp[(i, j)] = ignore or use
                return dp[(i, j)]

            if match:
                dp[(i, j)] = dfs(i + 1, j + 1)
                return dp[(i, j)]

            dp[(i, j)] = False
            return False

        return dfs(0, 0)