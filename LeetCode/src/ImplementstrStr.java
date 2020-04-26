/**
 * 28. 实现 strStr()
 */
public class ImplementstrStr {

    public static void main(String[] args) {
        String haystack = "hello", needle = "ll";

        int i = strStr(haystack, needle);
        System.out.println(i);
    }


    public static int strStr(String haystack, String needle) {

        for (int i = 0; i < haystack.length() - needle.length(); i++) {
            if (haystack.substring(i, needle.length()+1).equals(needle)) {
                return i;
            }
        }



        return -1;
    }
}
