class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest = len(strs[0])
        for word in strs:
            length = len(word)
            if longest > length:
                longest = length
            for i in range(longest):
                if word[i] != strs[0][i]:
                    longest = i
                    if longest <= 0:
                        return ""
                    break
        return strs[0][:longest]
