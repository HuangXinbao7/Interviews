/**
 * 1.TwoSum
 */
public class TwoSum {

    public static void main(String[] args) {
        int[] nums = new int[]{2,7,11,15};
        int target = 9;
        Solution solution = new Solution();
        int[] res = solution.twoSum(nums, target);
        for(int i: res){
            System.out.println(i);
        }
    }
}


class Solution {

    public int[] twoSum(int[] nums, int target) {
        int[] res = new int[2];
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if(nums[i] + nums[j] == target) {

                    res[0] = 1;
                    res[1] = 2;
                }
            }
        }
        return res;
    }
}