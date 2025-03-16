# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        string_of_list = ""
        while (head):
            string_of_list += str(head.val)
            head = head.next

        if (string_of_list == string_of_list[::-1]):
            return True
        return False

