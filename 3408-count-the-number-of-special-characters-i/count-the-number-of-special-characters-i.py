class Solution(object):
    def numberOfSpecialChars(self, word):
        s = set() 
        for i in word:
            for j in word:
                if i != j and i == j.upper():
                    s.add(i.lower())
        return len(s)

