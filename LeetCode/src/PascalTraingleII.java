import com.sun.deploy.security.SelectableSecurityManager;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * 119. 杨辉三角 II
 * 给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
 *
 * 在杨辉三角中，每个数是它左上方和右上方的数的和。
 *
 * 示例:
 * 输入: 3
 * 输出: [1,3,3,1]
 * 进阶：
 * 你可以优化你的算法到 O(k) 空间复杂度吗？
 */
public class PascalTraingleII {

    public static void main(String[] args) {

        List<Integer> row = getRow(3);
        System.out.println(row);
    }


    public static List<Integer> getRow(int rowIndex) {
        List<Integer> pre = new ArrayList<>();
        List<Integer> cur = new ArrayList<>();

        for (int i = 0; i <= rowIndex; i++) {
            cur = new ArrayList<>();
            for (int j = 0; i <= i; j++) {
                if (j == 0 || j == i) {
                    cur.add(1);
                }else {
                    cur.add(pre.get(j - 1) + pre.get(i));
                }
            }
            pre = cur;
        }
        return cur;
    }
}
