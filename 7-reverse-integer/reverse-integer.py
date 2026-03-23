class Solution(object):
    def reverse(self, x):
        if x < 0:
            s = str(-x)
            s = s[::-1]
            res = -int(s)
        else:
            s = str(x)
            s = s[::-1]
            res = int(s)
        if res < -2**31 or res > 2**31 - 1:
            return 0

        return res