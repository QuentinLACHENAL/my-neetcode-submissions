class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_idx = 0
        t_idx = 0
        while s_idx < len(s):
            if t_idx == len(t):
                return False
            if s[s_idx] == t[t_idx]:
                s_idx += 1
            t_idx += 1
        return True
