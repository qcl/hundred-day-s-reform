# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def DFSwithRange(left, node, right):
            if node == None:
                return None
            
            mins = []
            if left != None:
                mins.append(abs(left - node.val))
            if right != None:
                mins.append(abs(right - node.val))
            
            mins.append(DFSwithRange(left, node.left, node.val))
            mins.append(DFSwithRange(node.val, node.right, right))

            return min(filter(lambda x: x != None, mins))
            
        return DFSwithRange(None, root, None)
