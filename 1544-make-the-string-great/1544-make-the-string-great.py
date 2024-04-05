class Solution:
    def makeGood(self, s: str) -> str:
        word = []
        for char in s:
            if word and (word[-1] == char.swapcase()):
                word.pop() # deleting the added one and not adding the new one
            else:
                word.append(char)
        return ''.join(word)        


        