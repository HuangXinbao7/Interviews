package algorithms;

import com.sun.scenario.effect.Brightpass;

import java.util.Arrays;

/**
 * 27. 移除元素
 */
public class RemoveElement {

    public static void main(String[] args) {

        //int[] nums = new int[]{3,2,2,3};
        int[] nums = new int[]{0,1,2,2,3,0,4,2};
        int val = 2;

        int i = removeElement(nums, val);
        System.out.println(i);
    }


    /**
     * 解法1
     */
    public static int removeElement(int[] nums, int val) {

        int right = nums.length - 1;
        for (int left = nums.length - 1; left > -1; left--) {
            if (nums[left] == val) {
                int tmp = nums[left];
                nums[left] = nums[right];
                nums[right] = tmp;
                System.out.println("left: " + left + " right: " + right);
                right--;
            }
        }
        return right + 1;
    }


    /**
     * 第二种思路
     * 标签：交换移除
     * 主要思路是遍历数组nums，遍历指针为i，总长度为ans
     * 在遍历过程中如果出现数字与需要移除的值不相同时，则i自增1，继续下一次遍历
     * 如果相同的时候，则将nums[i]与nums[ans-1]交换，
     * 即当前数字和数组最后一个数字进行交换，交换后就少了一个元素，故而ans自减1
     * 这种思路在移除元素较少时更适合使用，最极端的情况是没有元素需要移除，遍历一遍结束即可
     * 时间复杂度：O(n)，空间复杂度：O(1)
     */
    public int removeElement2(int[] nums, int val) {
        int ans = nums.length;
        for (int i = 0; i < ans;) {
            if (nums[i] == val) {
                nums[i] = nums[ans - 1];
                ans--;
            } else {
                i++;
            }
        }
        return ans;
    }
}
