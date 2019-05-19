"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head == None:
            return None

        node_id = 0
        node_to_id = {None: None}
        copied = {None: None}

        current_node = head
        while current_node != None:
            copied_node = Node(current_node.val, None, None)
            copied[node_id] = copied_node
            node_to_id[current_node] = node_id
            current_node = current_node.next
            node_id = node_id + 1

        current_node = head
        node_id = 0
        while current_node != None:
            copied_node = copied[node_id]
            next_node_id = node_to_id[current_node.next]
            copied_node.next = copied[next_node_id]
            random_node_id = node_to_id[current_node.random]
            copied_node.random = copied[random_node_id]
            current_node = current_node.next
            node_id = node_id + 1

        return copied[0]
