class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # if '.' not in s and '*' not in p:
        #     if s == p:
        #         return True
        #     else:
        #         return False

        ans = self.match(s, p)
        return ans

    def match(self, s, p):
        '''
            '.' Matches any single character.
            '*' Matches zero or more of the preceding element
        '''
        if p[-1] == '*':
            if s[-1] == p[-2] or p[-2] == '.':
                s = s[:-1]
                return self.match(s, p)
            else:
                s = s[:-1]
                p = p[:-1]
                return self.match(s, p)
        if s[-1] == p[-1]:
            s = s[1:]
            p = p[1:]
            return self.match(s, p)
        else:
            return False


if __name__ == '__main__':
    '''
    '.' Matches any single character.
    '*' Matches zero or more of the preceding element
    '''
    solution = Solution()
    s = 'aab'
    p = 'aa'

    ans = solution.isMatch(s, p)
    print(ans)
