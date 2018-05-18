# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        if head == None:
            return head

        last = head
        length = 1
        while last.next != None:
            length += 1
            last = last.next

        k = k % length

        move = length - k
        last.next = head

        while move > 0:
            move -= 1
            last = head
            head = head.next

        last.next = None

        return head
