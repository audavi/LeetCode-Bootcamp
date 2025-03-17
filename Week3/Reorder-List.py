# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head.next
        while fast and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        second = slow.next  # will be head of the 2nd half
        slow.next = None

        # reverse 2nd half
        before = None
        while second:
            after = second.next
            second.next = before
            before = second
            second = after

        first = head
        second = before
        while second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2

