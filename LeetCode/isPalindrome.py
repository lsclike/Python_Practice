class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        strx = str(x)
        if len(strx) % 2 != 0:
            for n in range(len(strx)//2):
                if int(strx[n]) != int(strx[len(strx) - n]):
                    return False
            return True
        else:
            head = 0
            trail = len(strx) - 1
            while trail > head:
                if int(strx[head]) != int(strx[trail]):
                    return False
                head += 1
                trail -= 1
            return True