class Solution(object):
    def strStr(self, haystack, needle):
        s = len(needle)
        for i in range(len(haystack)):
            if haystack[i]== needle[0]:
               if haystack[i:i+s] == needle:
                return i
        return -1
