class Solution(object):
    def minDeletionSize(self, strs):
        rows=len(strs)
        cols=len(strs[0])
        delete = 0

        for c in range(cols):
            for r in range(1,rows):
                if strs[r][c] < strs[r-1][c]:
                    delete = delete +1
                    break
        return delete
        