class Solution(object):
    def increasingTriplet(self, nums):
        first = float('Inf')
        second = float('Inf')

        for num in nums:
            if num <= first:
                first = num
            elif num<= second:
                second = num
            else:
                return True
        return False
        