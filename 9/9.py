class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        xLenMiddle = len(x) // 2
        xLenRemainder = len(x) % 2
        # 奇數
        if xLenRemainder != 0:
            index = xLenMiddle - 1
            index2 = xLenMiddle + 1
        # 偶數
        else:
            index = xLenMiddle - 1
            index2 = xLenMiddle

        for i in range(xLenMiddle):
            if i != 0:  # first don't do
                index -= 1
                index2 += 1

            if x[index] != x[index2]:
                return False

        return True


'''
def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return str(x) == str(x)[::-1]
        '''
if __name__ == '__main__':
    '''
    確認是否為回文
    '''
    solution = Solution()
    x = 123
    ans = solution.isPalindrome(x)
    print(ans)
