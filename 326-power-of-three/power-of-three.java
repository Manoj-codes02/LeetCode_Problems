class Solution {

    public boolean isPowerOfThree(int n) {

        int num = 1;

        for (int i = 0; i <= 20; i++) {

            if (n == num) {
                return true;
            }

            num = num * 3;
        }

        return false;
    }
}