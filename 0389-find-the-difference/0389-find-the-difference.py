class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s1 = 0
        s2 = 0
        for char1 in  s:
            s1 += ord(char1)
        for char2 in  t:
            s2 += ord(char2)
        return chr(s2 -s1)    