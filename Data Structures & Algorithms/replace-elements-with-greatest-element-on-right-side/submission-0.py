class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        biggest = arr[len(arr) - 1]
        L = len(arr) - 2
        while L >= 0:
            tmp = arr[L]
            arr[L] = biggest
            if tmp > biggest:
                biggest = tmp
            L -= 1
        arr[len(arr) - 1] = -1
        return arr