"""
Given the root of a complete binary tree, return the number of the nodes in the tree.
According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree,
and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.
Design an algorithm that runs in less than O(n) time complexity.

Example 1:
    Input: root = [1,2,3,4,5,6]
    Output: 6

Example 2:
    Input: root = []
    Output: 0

Example 3:
    Input: root = [1]
    Output: 1
"""

class TreeNode:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None


def countNodes(root):
    def inOrder(node):
        if not node:
            return 0
        left = inOrder(node.left)
        right = inOrder(node.right)

        return 1 + left + right
    
    return inOrder()


root = TreeNode(1)
node1 = TreeNode(2)
node2 = TreeNode(3)
node3 = TreeNode(4)
node4 = TreeNode(5)
node5 = TreeNode(6)

root.left = node1
root.right = node2
root.left = node3
root.right = node4
root.left = node5