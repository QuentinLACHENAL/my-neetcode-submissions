class Solution:
    def reverseString(self, s: List[str]) -> None:
        lenght = len(s)
        for i in range(int(lenght / 2)):
            tmp = s[i]
            s[i] = s[lenght - 1 - i]
            s[lenght - 1 - i] = tmp