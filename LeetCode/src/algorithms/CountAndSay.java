package algorithms;

import java.util.Arrays;

/**
 *
 */
public class CountAndSay {

    public static void main(String[] args) {

        String s = countAndSay(3);
        //System.out.println(s);

    }

    public static String countAndSay(int n) {
        String pre = "1";
        String cur = "";

        if (n == 1) return pre;
        char[] chars = pre.toCharArray();
        for (int i = 0; i < chars.length; i++) {
            //chars.
        }



        return cur;
    }
}
