# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Iteration
        curr = head
        prev = None
        # Traverse all the nodes of Linked List
        while curr is not None:

            # Store next
            nextNode = curr.next

            # Reverse current node's next pointer
            curr.next = prev

            # Move pointers one position ahead
            prev = curr
            curr = nextNode

        # Return the head of reversed linked list
        return prev

        # T: O(n)
        # S: O(1)