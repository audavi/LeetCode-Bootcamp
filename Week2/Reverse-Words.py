class Solution(object):
    def reverseWords(self, s):
        rev = s.split()
        ans = " ".join(reversed(rev))
        return ans
