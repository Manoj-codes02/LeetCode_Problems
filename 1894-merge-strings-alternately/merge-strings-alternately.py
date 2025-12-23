class Solution(object):
    def mergeAlternately(self, word1, word2):
        result= ""
        i=0

        while i<len(word1) and i<len(word2):
            result = result + word1[i]
            result = result + word2[i]
            i=i+1

        result=result + word1[i:]
        result=result + word2[i:]

        return result