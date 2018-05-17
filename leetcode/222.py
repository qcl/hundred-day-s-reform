# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def countSubTreeNodes(rootNode):
            if rootNode == None:
                return 0
            r = rootNode
            l = rootNode
            level = 0
            while not r.right == None:
                r = r.right
                l = l.left
                level += 1
            if l == None:
                return 2**(level+1) - 1

            return countSubTreeNodes(rootNode.left) + 1 + countSubTreeNodes(rootNode.right) 

        return countSubTreeNodes(root)
