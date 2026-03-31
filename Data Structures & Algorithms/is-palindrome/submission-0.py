class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.strip().lower()
        print(s)
        s = "".join(c for c in s if c.isalnum())
        length = len(s)
        for i in range(int(length / 2)):
            if s[i] != s[length - 1 - i]:
                return False
        return True
