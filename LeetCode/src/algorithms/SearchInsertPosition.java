package algorithms;

import java.util.Arrays;

/**
 * 35. 搜索插入位置
 */
public class SearchInsertPosition {

    public static void main(String[] args) {

         //int[] nums = new int[]{1,3,5,6};
         int[] nums = new int[]{1,3,5,6};
         int target = 6;



        int i = searchInsert(nums, target);
        System.out.println(i);
    }

    public static int searchInsert(int[] nums, int target) {
        int ins = -1;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == target) {
                ins = i;
            }else if (nums[i] < target) {
                i++;
            } else if (nums[i] > target){
                return i - 1;
            } else {
                return i;
            }
        }
        return ins;
    }
}
