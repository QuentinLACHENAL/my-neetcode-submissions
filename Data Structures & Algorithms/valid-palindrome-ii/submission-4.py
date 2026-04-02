class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0
        last = len(s) - 1
        while i <= last:
            if s[i] == s[last]:
                i += 1
                last -= 1
            else:
                if self.isPalindrome(s, i + 1, last):
                    print("1")
                    return True
                elif self.isPalindrome(s, i, last - 1):
                    print("2")
                    return True
                else:
                    return False
                    
        return True
             

    def isPalindrome(self, s, i, last) -> bool:
        if i == len(s) or last < 0:
            return False
        while i <= last:
            if s[i] == s[last]:
                i += 1
                last -= 1
            else:
                return False
        return True

             