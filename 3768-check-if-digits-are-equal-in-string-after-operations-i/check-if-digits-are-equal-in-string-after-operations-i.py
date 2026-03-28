class Solution(object):
    def hasSameDigits(self, s):
        while len(s) > 2:
            result = ""   
            for i in range(len(s) - 1):
                val = (int(s[i]) + int(s[i+1])) % 10
                result += str(val)
            s = result   
        
        return s[0] == s[1]