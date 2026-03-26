class Solution(object):
    def triangleType(self, nums):
        a = nums[0]
        b = nums[1]
        c = nums[2]

        if a+b<=c or a+c<=b or b+c<=a:
            return "none"
            
        if a==b==c:
            return "equilateral"
        elif (a==b) or (a==c) or (b==c):
            return "isosceles"
        else:
            return "scalene"




        