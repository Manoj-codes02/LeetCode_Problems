class Solution(object):
    def sortPeople(self, names, heights):
        result = []

        for i in range(len(names)):
            result.append([heights[i] , names[i]])

        result.sort(reverse=True)

        ans = []
        for pair in result:
            ans.append(pair[1])

        return ans