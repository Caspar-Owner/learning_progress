class Solution(object):
    def isPalindrome(self, x):
        self.x = x
        a = str(x)[::-1]
        if x < 0:
            return False
        elif str(x) == a:
            return True
        else:
            return False     