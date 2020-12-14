package algorithms;

import java.util.Arrays;

/**
 * 35. 搜索插入位置
 */
public class SearchInsertPosition {

    public static void main(String[] args) {

         int[] nums = new int[]{1,3,5,6};
         int target = 7;

        int i = searchInsert(nums, target);
        System.out.println(i);
    }

    /**
     *
     */
    public static int searchInsert(int[] nums, int target) {
        for (int i = nums.length - 1; i > -1;) {
            if (target == nums[i]) {
                return i;
            } else if(target > nums[i]) {
                return i + 1;
            } else {
                i--;
            }
        }
        return 0;
    }
}
