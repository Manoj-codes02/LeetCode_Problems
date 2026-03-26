class Solution(object):
    def findMissingElements(self, nums):
        n = len(nums)
        result = []
        mn = min(nums)
        mx = max(nums)
        for i in range(mn,mx+1):
            if i not in nums:
                result.append(i)
        return result