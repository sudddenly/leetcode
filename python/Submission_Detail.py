class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        s = ''
        for i in str:
            if ord(i) >= ord('A') and ord(i) <= ord('Z'):
                s = s + chr(ord(i) - ord('A') + ord('a'))
            else:
                s = s + i
        return s