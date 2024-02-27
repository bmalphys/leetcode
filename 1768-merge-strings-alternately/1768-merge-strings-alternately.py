class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        my_str = ''
        min_len = min(len(word1), len(word2))
        for i in range(min_len):
            my_str = my_str + word1[i] + word2[i]
        if (len(word1) <= len(word2)):            
            my_str = my_str + word2[i+1:]
        else:
            my_str = my_str + word1[i+1:]     
        return my_str    
        