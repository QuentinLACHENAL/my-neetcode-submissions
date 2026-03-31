# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        currentNode = head
        previousNode = None
        while currentNode:
            tmp = currentNode.next
            currentNode.next = previousNode
            previousNode = currentNode
            currentNode = tmp
        head = previousNode
        return head