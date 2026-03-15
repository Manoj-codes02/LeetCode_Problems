class Solution(object):
    def removeStars(self, s):
        result = ""
        for i in s:
            if i== "*":
                result = result[:-1]
            else:
                result += i
        return result