class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        temp = str(x)
        if temp[0] == '-':
            # temp = temp[1:]
            a ='-' + temp[:0:-1]
        else:
            a = temp[::-1]
        if int(a) > 2147483647:
            return int(0)
        else:
            return int(a)

if __name__ == '__main__':
    sol = Solution()
    sol.reverse(-234)