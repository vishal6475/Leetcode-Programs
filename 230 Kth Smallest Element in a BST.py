# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.count = 0
        def inOrder(node):
            if node.left != None:
                lv = inOrder(node.left) 
                if lv != None: return lv

            self.count += 1
            if self.count == k: return node.val
            if node.right != None:
                rv = inOrder(node.right) 
                if rv != None: return rv

        kValue = inOrder(root)

        return kValue