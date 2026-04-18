class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashMapS = {}
        hashMapT = {}
        for c in s:
            hashMapS[c] = 1 + hashMapS.get(c, 0)
        for c in t:
            hashMapT[c] = 1 + hashMapT.get(c, 0)
        if hashMapS == hashMapT:
            return True
        return False