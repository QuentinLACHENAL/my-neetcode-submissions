class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        tlist = []
        if len(s) != len(t):
            return False
        for c in t:
            tlist.append(c)
        for c in s:
            if c in tlist:
                tlist.remove(c)
        if len(tlist) == 0:
            return True
        return False
