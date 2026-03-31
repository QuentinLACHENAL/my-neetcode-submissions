class Solution:
    def reverseString(self, s: List[str]) -> None:
        lenght = len(s)
        for i in range(int(lenght / 2)):
            s[i], s[lenght - 1 - i] = s[lenght - 1 - i], s[i]