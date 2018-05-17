# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        
        if head == None:
            return None
    
        items = [head.val]

        while not head.next == None:
            head = head.next
            items.append(head.val)
        
        def buildSubTree(itemList):
            if len(itemList) == 1:
                return TreeNode(itemList[0])
            elif len(itemList) == 2:
                tn = TreeNode(itemList[1])
                tn.left = TreeNode(itemList[0])
                return tn

            middleIndex = int(len(itemList)/2)
            leftItems = itemList[:middleIndex]
            rightItems = itemList[middleIndex + 1:]
            tn = TreeNode(itemList[middleIndex])
            tn.right = buildSubTree(rightItems)
            tn.left = buildSubTree(leftItems)
    
            return tn

        return buildSubTree(items)
