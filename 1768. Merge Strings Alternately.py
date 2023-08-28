class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged_word = ""

        if len(word1)>len(word2):
            for i in range(len(word2)):
                merged_word += word1[i] + word2[i]
            merged_word += word1[len(word2):]
        else:
            for i in range(len(word1)):
                merged_word += word1[i] + word2[i]
            merged_word += word2[len(word1):]

        return merged_word