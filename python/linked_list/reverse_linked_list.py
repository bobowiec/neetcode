# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    # Time complexity: O(n), space complexity: O(n)
    # Recursive version
    def reverseListRecursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        new_head = head
        if head.next:
            new_head = self.reverseList(head.next)
            head.next.next = head
        head.next = None

        return new_head

    # Time complexity: O(n), space complexity: O(n)
    # Recursive version
    def reverseListRecursiveNotOpt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(prev: Optional[ListNode], cur: Optional[ListNode]):
            if not cur:
                return prev

            next = cur.next
            cur.next = prev

            return reverse(cur, next)
            
        return reverse(None, head)

    # Time complexity: O(n), space complexity: O(1)
    # Iterative version
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            # Pythonic version
            # curr.next, prev, curr = prev, curr, curr.next
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev
 
