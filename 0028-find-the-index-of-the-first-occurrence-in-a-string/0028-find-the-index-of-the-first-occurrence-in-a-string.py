class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        myindex = -1
        len_needle = len(needle)
        len_haystack = len(haystack)
        for i in range(len_haystack - len_needle + 1):
            if needle == str(haystack[i: i + len_needle]): 
                myindex = i
                break
        return myindex