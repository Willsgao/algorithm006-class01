# 验证回文字符串2
class Solution(object):
    def validPalindrome(self,s):
        p1,p2 = 0,len(s)-1
        while p1 < p2:
            if s[p1] != s[p2]:
                a = s[p1+1:p2+1]
                b = s[p1:p2]
                return a[::-1] == a or b[::-1] == b
            p1 += 1
            p2 -= 1
        return True