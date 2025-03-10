class Solution(object):
    def myAtoi(self, s):
        left = 0
        s = s.lstrip()

        if len(s) == 0:
            return 0

        sign = 1
        if s[0] == '-':
            sign = -1
            left = 1
        elif s[0] == '+':\
            left = 1

        result = 0
        ind = left
        while ind < len(s):
            if not('0' <= s[ind] <= '9'):
                return result * sign

            result = result * 10 + ord(s[ind]) - ord('0')
            min_val = -2 ** 31
            max_val = 2 **(31-1)
            if result * sign <= min_val:
                return -min_val
            elif result * sign >= max_val:
                return max_val
            ind += 1
        return result * sign