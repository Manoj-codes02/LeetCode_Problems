class Solution(object):
    def getCommon(self, nums1, nums2):
        left = 0
        right = 0

        while left < len(nums1) and right < len(nums2):
            if nums1[left] == nums2[right]:
                return nums1[left]

            elif nums1[left] < nums2[right]:
                left += 1

            else:
                right += 1
        return -1