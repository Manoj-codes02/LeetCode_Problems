class Solution(object):
    def findWords(self, words):
        first = "qwertyuiop"
        second = "asdfghjkl"
        third = "zxcvbnm"
        
        res = []
        
        for word in words:
            w = word.lower()
            
            # check first row
            ok = True
            for c in w:
                if c not in first:
                    ok = False
                    break
            if ok:
                res.append(word)
                continue
            
            ok = True
            for c in w:
                if c not in second:
                    ok = False
                    break
            if ok:
                res.append(word)
                continue

            ok = True
            for c in w:
                if c not in third:
                    ok = False
                    break
            if ok:
                res.append(word)
        
        return res