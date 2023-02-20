# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        minn = float('-inf')
        maxx = float('inf')

        def isValid(node, mn, mx):
            if node.val < mn or node.val > mx:
                return False
            if node.left != None:
                if not isValid(node.left, mn, min(mx, node.val)-1):
                    return False
            if node.right != None:
                if not isValid(node.right, max(mn, node.val)+1, mx):
                    return False
            return True

        return isValid(root, minn, maxx)