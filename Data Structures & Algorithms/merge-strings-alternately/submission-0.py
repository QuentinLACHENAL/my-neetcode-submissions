class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        newWord = [""] * (len(word1) + len(word2))
        i = 0
        j = 0
        k = 0
        while i < len(word1) and j < len(word2):
            newWord[k] = word1[i]
            i += 1
            newWord[k + 1] = word2[j]
            j += 1
            k += 2
        while i < len(word1):
            newWord[k] = word1[i]
            i += 1
            k += 1
        while j < len(word2):
            newWord[k] = word2[j]
            j += 1
            k += 1
        newWordStr = "".join(newWord)
        return newWordStr