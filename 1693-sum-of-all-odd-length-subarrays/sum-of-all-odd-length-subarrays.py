class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        total = 0 
        n = len(arr)

        for i in range(n):
            left = i+1
            right = n-i
            
            total_sub = left*right
            odd = (total_sub+1)//2
            
            total += arr[i]*odd
        return total