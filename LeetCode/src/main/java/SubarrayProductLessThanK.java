import java.util.Arrays;
import java.util.Map;

/**
 * 713. 乘积小于K的子数组
 *
 * 给定一个正整数数组 nums。找出该数组内乘积小于 k 的连续的子数组的个数。
 *
 * 示例 1:
 * 输入: nums = [10,5,2,6], k = 100
 * 输出: 8
 * 解释: 8个乘积小于100的子数组分别为: [10], [5], [2], [6], [10,5], [5,2], [2,6], [5,2,6]。
 * 需要注意的是 [10,5,2] 并不是乘积小于100的子数组。
 *
 * 说明:
 * 0 < nums.length <= 50000
 * 0 < nums[i] < 1000
 * 0 <= k < 10^6
 */
public class SubarrayProductLessThanK {

    public static void main(String[] args) {

        int[] nums = new int[]{10, 5, 2, 6};
        //int k = 100;

        // 随机的长度和k
        int[] randNums = new int[1 + (int)(Math.random() * 50000)];
        for(int i = 0; i < randNums.length; i++) {
            randNums[i] = (int)(1 + Math.random() * 999);
        }
        int k = (int)(Math.random() * 1000000);

        int i = numSubarrayProductLessThanK(randNums, k);
        System.out.println(i);
    }


    /**
     * 思路：使用双指针
     * 核心思想：
     * 始终保证当前窗口中乘积小于k。
     * 当前窗口下的乘积小于k等价于当前窗口下子数组的各个连续子数组乘积也小于k。
     * 举个例子：当窗口为[10,5,2]时，1052<k，那么随便从其中拿出两个或一个或三个是不是都小于k。
     * 接下来这里有个很重要的条件是要连续的子数组也就是说[10,5,2]中不能取[10,2]因为不连续。
     *
     * 思路很明显了：
     * 1.使用变量times存储个数
     * 2.我们让右指针不断前进，当窗口乘积小于k时，就让times+=窗口连续子数组个数
     * 3.当窗口乘积大于等于k时，我们就让乘积去除左指针对应的值，然后左指针右移，直至乘积小于k。
     * 那么窗口中连续子数组的个数是多少呢？
     * times+=right-left+1
     * 比如例子中[10, 5, 2, 6]，初始情况窗口中只有10，所以times+1，
     * 之后窗口中加上了5，变成[10,5],其中连续子数组有：{{10},{5},{10,5}}，
     * 之前的10已经加过了，因此每次加进去的连续子数组是以当前right对应的数为首的连续子数组，
     * 再以[10,5,2]，以2为首就是{2,25,2510},对应为right-left+1。
     */
    public static int numSubarrayProductLessThanK(int[] nums, int k) {

        if (k <= 1) return 0;
        int now = 1, times = 0, left = 0;
        for(int right = 0; right < nums.length; right++) {
            now *= nums[right];
            while (now >= k) now /= nums[left++];

            /*
            * 关键是知道这个等式怎么来的
            * right左边的元素均已经考虑了所有的组合, 所以只要考虑含right的组合
            * 显然含right的组合数刚好是子数组的长度
            * 举个例子：[...5,6,3,4,8,...]
            * 假设right遍历到了数值8的位置, left经过摘除后移到了数值5处
            * 此时所有的组合情况是:
            * [56348]
            * [6348]
            * [348]
            * [48]
            * [8]
            * 共5种
            * */
            times += right - left + 1;
        }
        return times;
    }
}
