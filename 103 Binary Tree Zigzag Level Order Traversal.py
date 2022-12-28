
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def traverseLevels(self, node, level):
        if level > len(self.values):
            self.values.append([node.val])
        else:
            self.values[level-1].append(node.val)
        
        if node.left is not None:
            self.traverseLevels(node.left, level + 1)
        if node.right is not None:
            self.traverseLevels(node.right, level + 1)

    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        self.values = []
        self.level = 1

        self.traverseLevels(root, self.level)

        for i in range(1, len(self.values)):
            if i % 2 == 1:
                self.values[i].reverse()

        return self.values
        