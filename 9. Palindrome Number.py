class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        l = len(str(x))
        rev = 0
        i = 0
        while x > 0 and i < l // 2:
            mod = x % 10
            rev = (rev * 10) + mod
            x = x // 10
            i+=1
        if l % 2 == 0:
            if rev == x:
                return True
            else:
                return False
        else:
            x = x // 10
            if rev == x:
                return True
            else:
                return False
