# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.totalMaxSum = float('-inf')

        def maxSum(node):
            left, right = float('-inf'), float('-inf')
            if node.left != None:
                left = maxSum(node.left)
            if node.right != None:
                right = maxSum(node.right)

            self.totalMaxSum = max(self.totalMaxSum, node.val + left + right, left, right)

            return max(node.val + left, node.val + right, node.val)


        return max(maxSum(root), self.totalMaxSum)