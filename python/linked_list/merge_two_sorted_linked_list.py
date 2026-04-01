# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    # Time complexity: O(n + m), Space complexity: O(n + m)
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        
        if not list2:
            return list1
        
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
    
    # Time complexity: O(n + m), Space complexity: O(1)
    def mergeTwoListsIteratively(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = node = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next
        
        node.next = list1 or list2

        return dummy_node.next            
 
    # Time complexity: O(n + m), Space complexity: O(1)
    def mergeTwoLists2(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head, prev, node = None, None, None

        while list1 and list2:
            prev = node
            if list1.val < list2.val:
                node = list1
                list1 = list1.next
            else:
                node = list2
                list2 = list2.next
            if not head:
                head = node
            else:
                prev.next = node

        while list1:
            prev = node
            node = list1
            if not head:
                head = node
            else:
                prev.next = node
            list1 = list1.next
        
        while list2:
            prev = node
            node = list2
            if not head:
                head = node
            else:
                prev.next = node
            list2 = list2.next
        
        return head
