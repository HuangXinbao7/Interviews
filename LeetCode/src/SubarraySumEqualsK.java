/**
 * 560. 和为K的子数组
 * 给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。
 *
 * 示例 1 :
 * 输入: nums = [1,1,1], k = 2
 * 输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。
 *
 * 说明 :
 * 数组的长度为 [1, 20,000]。
 * 数组中元素的范围是 [-1000, 1000] ，且整数 k 的范围是 [-1e7, 1e7]。
 */
public class SubarraySumEqualsK {

    public static void main(String[] args) {

        int[] nums = new int[]{1,2,3,4,5,6};
        int[] nums2 = {1};
        int k = 9;

        int i = subarraySum(nums, 9);
        System.out.println(i);
    }


    public static int subarraySum(int[] nums, int k) {

        int now = 0,  times= 0, left = 0;
        for (int right = 0; right < nums.length; right++) {
            now += nums[right];
            for (left = 0; left < right; left++) {
                int tmp = now;
                if (tmp == k) {
                    times++;
                }
                tmp -= nums[left];
            }
        }

        return times;
    }
}
