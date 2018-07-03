/*
        https://leetcode.com/problems/string-to-integer-atoi/description/
        Implement atoi which converts a string to an integer.
        The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.
        The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.
        If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.
        If no valid conversion could be performed, a zero value is returned.
*/
class Solution {
    public int myAtoi(String str) {
        // Runtime: 40 ms

        int sign = 1, total = 0, index = 0, len = str.length();
        if(len == 0){
            return 0;             // 空字符，返回0
        }

        while (index < len && str.charAt(index) == ' ' ) ++index;
        // 返回index处字符，空格字符忽略

        if(index < len && (str.charAt(index) == '+' || str.charAt(index) == '-')){
            sign = str.charAt(index++) == '+'? 1:-1;
            // + 表示正、-表示负
        }

        while (index < len){
            int digit = str.charAt(index) - '0';
            if(digit < 0 || digit > 9){
                break;
            }
            // 判断最后一位数字， 2147483647 ~ -2147483648, 另一种方法
            // if (total > Integer.MAX_VALUE / 10
            //                    || (total == Integer.MAX_VALUE / 10 && (sign == 1 && digit > 7 || sign == -1 && digit > 8)))
            if(Integer.MAX_VALUE / 10 < total || Integer.MAX_VALUE /10 == total && Integer.MAX_VALUE % 10 < digit){
                return sign == 1? Integer.MAX_VALUE : Integer.MIN_VALUE;
            }

            total = total * 10 + digit;
            ++ index;
        }
        return total * sign;
    }
}