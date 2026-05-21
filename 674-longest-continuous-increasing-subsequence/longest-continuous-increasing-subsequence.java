class Solution {
    public int findLengthOfLCIS(int[] nums) {
        int current_length = 1;
        int max_length = 1;

        for(int i=1; i<nums.length; i++){
            if (nums[i] > nums[i-1]){
               current_length++;
               max_length = Math.max(current_length , max_length);

            }
            else{
                current_length = 1;
            }
        }
        return max_length;


    }
}