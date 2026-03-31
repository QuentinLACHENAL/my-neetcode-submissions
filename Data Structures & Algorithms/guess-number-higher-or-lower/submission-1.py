# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        pick = n // 2
        L = 1
        R = n
        while(True):
            ret = guess(pick)
            if ret < 0:
                R = pick - 1
                pick = L + (R - L) // 2
            elif ret > 0:
                L = pick + 1
                pick = L + (R - L) // 2
            else:
                return pick