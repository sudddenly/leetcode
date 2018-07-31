# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        length = 0
        head2 = head
        while(head2 != None):
            head2 = head2.next
            length += 1
        for i in range(length//2):
            head = head.next
        return heads