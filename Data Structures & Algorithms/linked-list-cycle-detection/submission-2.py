# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hashMap = {}
        i = 0
        if not head:
            return False
        while head.next:
            if head in hashMap:
                return True
            hashMap[head] = i
            i += 1
            head = head.next
        return False