class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        myindex = -1
        for i in range(len(haystack) - len(needle) + 1):
            if needle == str(haystack[i: i + len(needle)]): 
                myindex = i
                break
        return myindex