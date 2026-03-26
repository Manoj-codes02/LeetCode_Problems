class Solution(object):
    def toggleLightBulbs(self, bulbs):
        result = []

        for i in bulbs:
            if i in result:
                result.remove(i)
            else:
                result.append(i)
        
        result.sort()
        return result