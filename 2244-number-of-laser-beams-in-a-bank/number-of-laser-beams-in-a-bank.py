class Solution(object):
    def numberOfBeams(self, bank):
        prev = 0 
        total = 0 

        for row in bank:
            curr = row.count('1')

            if curr>0:
                total += prev *curr
                prev = curr
        return total